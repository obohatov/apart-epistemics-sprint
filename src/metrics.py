"""Final metrics from the blind matching workbook (unsealed key used only here)."""
import json, csv, math, collections, re, pathlib
from openpyxl import load_workbook
ROOT = pathlib.Path(__file__).resolve().parent.parent
def wilson(k, n, z=1.96):
    if n == 0: return (float('nan'),) * 2
    p = k / n; d = 1 + z*z/n; c = p + z*z/(2*n); h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)); return ((c-h)/d, (c+h)/d)
def fmt(k, n):
    lo, hi = wilson(k, n); return f"{k}/{n} = {k/n:.2f} [{lo:.2f}, {hi:.2f}]" if n else "–"
wb = load_workbook(ROOT/'annotation/matching/blind_matching_completed.xlsx')
key = json.load(open(ROOT/'annotation/matching/KEY_DO_NOT_OPEN.json'))
L = lambda p: {json.loads(l)['id']: json.loads(l) for l in open(p, encoding='utf-8')}
E = {k: L(ROOT/f'data/eval/{k}.jsonl') for k in ('D1_B', 'D1_C', 'D2_B', 'D2_C')}
def issue(fid):
    k = key[fid]; ds = 'D1' if k['object'].startswith('D1') else 'D2'
    return k['evaluator'], E[f"{ds}_{k['evaluator']}"][k['object']]['result']['issues'][k['issue_index']]
gold = list(csv.DictReader(open(ROOT/'annotation/blind/D1_gold_issues.csv', encoding='utf-8')))
for n, r in enumerate(gold, 1): r['gid'] = f"GI{n:02d}"
G = {r['gid']: r for r in gold}
out = []
# ---------------- D1
rows = [r for r in wb['D1_match'].iter_rows(values_only=True)][1:]
flags = collections.defaultdict(list); found = collections.defaultdict(set); sev_pairs = collections.defaultdict(list)
for r in rows:
    ev, it = issue(r[1]); lab = str(r[5]).strip().upper()
    gids = re.findall(r'GI\d+', lab)
    cat = 'GI' if gids else ('NEW' if lab.startswith('NEW') else 'FA')
    flags[ev].append((cat, it))
    for g in gids:
        found[ev].add(g); sev_pairs[ev].append((G[g]['severity'], it['severity']))
out.append("## D1 — issue level (18 gold answers, 33 gold issues)\n")
out.append("| | B | C |\n|---|---|---|")
for lbl, f in [("Flags raised", lambda ev: str(len(flags[ev]))),
               ("Flags matching a gold issue", lambda ev: fmt(sum(c == 'GI' for c, _ in flags[ev]), len(flags[ev]))),
               ("Flags that are real problems (gold or NEW)", lambda ev: fmt(sum(c != 'FA' for c, _ in flags[ev]), len(flags[ev]))),
               ("False alarms (FA)", lambda ev: fmt(sum(c == 'FA' for c, _ in flags[ev]), len(flags[ev]))),
               ("Gold issues found (recall)", lambda ev: fmt(len(found[ev]), len(gold))),
               ("Material gold issues found", lambda ev: fmt(len([g for g in found[ev] if G[g]['severity'] == 'material']), sum(r['severity'] == 'material' for r in gold))),
               ("Material flags that are FA", lambda ev: fmt(sum(c == 'FA' and i['severity'] == 'material' for c, i in flags[ev]), sum(i['severity'] == 'material' for _, i in flags[ev]))),
               ("Severity agreement on matched pairs", lambda ev: fmt(sum(a == b for a, b in sev_pairs[ev]), len(sev_pairs[ev])))]:
    out.append(f"| {lbl} | {f('B')} | {f('C')} |")
out.append("\nRecall by gold coarse type (diagnostic matrix):\n\n| Gold type | n | B | C | found by B only | by C only |\n|---|---|---|---|---|---|")
for t in ('factual', 'source', 'omission_or_framing'):
    ids = [r['gid'] for r in gold if r['coarse_type'] == t]
    b = [g for g in ids if g in found['B']]; c = [g for g in ids if g in found['C']]
    out.append(f"| {t} | {len(ids)} | {len(b)} | {len(c)} | {len(set(b)-set(c))} | {len(set(c)-set(b))} |")
fa_type = {ev: collections.Counter(i['coarse_type'] for c, i in flags[ev] if c == 'FA') for ev in 'BC'}
out.append(f"\nFalse alarms by flag coarse type: B {dict(fa_type['B'])}; C {dict(fa_type['C'])}.")
both = found['B'] & found['C']; onlyB = found['B'] - found['C']; onlyC = found['C'] - found['B']; none = set(G) - found['B'] - found['C']
out.append(f"\nGold issues found by both: {len(both)}; only B: {sorted(onlyB)}; only C: {sorted(onlyC)}; by neither: {sorted(none)}.")
# ---------------- D2
rows = [r for r in wb['D2_match'].iter_rows(values_only=True)][1:]
det = collections.defaultdict(dict); dsev = collections.defaultdict(dict)
for r in rows:
    ev, it = issue(r[2]); obj = r[0]
    det[ev].setdefault(obj, False)
    if str(r[5]).strip().lower() == 'yes':
        det[ev][obj] = True; dsev[ev].setdefault(obj, set()).add(it['severity'])
cards = json.load(open(ROOT/'data/D2/cards.json', encoding='utf-8'))
exp = {f"D2-{b['base'][3:]}-{p['type']}": p for b in cards['bases'] for p in b['perturbations']}
out.append("\n## D2 — perturbation detection (blind human matching)\n\n| Type | B | C | Expected |\n|---|---|---|---|")
for t in ('T1', 'T2', 'T3', 'T4', 'T5'):
    objs = [o for o in exp if o.endswith(t)]
    out.append(f"| {t} | {sum(det['B'].get(o, False) for o in objs)}/6 | {sum(det['C'].get(o, False) for o in objs)}/6 | {exp[objs[0]]['expected_detectors']} |")
miss = {ev: sorted(o[3:] for o in exp if not o.endswith('T5') and not det[ev].get(o, False)) for ev in 'BC'}
out.append(f"\nMissed (T1–T4): B {miss['B']}; C {miss['C']}.")
sevok = {ev: sum(1 for o, s in dsev[ev].items() if not o.endswith('T5') and exp[o]['expected_severity'] in s) for ev in 'BC'}
ndet = {ev: sum(1 for o in dsev[ev] if not o.endswith('T5')) for ev in 'BC'}
out.append(f"Detected perturbations rated with the expected severity: B {sevok['B']}/{ndet['B']}; C {sevok['C']}/{ndet['C']}.")
auto = {(r['evaluator'], r['object']): r['detected'] == 'True' for r in csv.DictReader(open(ROOT/'analysis/d2_auto_detection.csv', encoding='utf-8'))}
agree = sum(auto[(ev, o)] == det[ev].get(o, False) for ev in 'BC' for o in exp)
out.append(f"Agreement of the automatic first pass with blind human matching: {agree}/60.")
(ROOT/'analysis/final_metrics.md').write_text("# Final metrics (blind matching)\n\n" + "\n".join(out) + "\n", encoding='utf-8')
print("\n".join(out))
