"""Automatic first-pass detection of D2 perturbations (to be confirmed by blind human matching).
A perturbation counts as detected by an evaluator if one of its issues
 (a) quotes text inserted by the edit (>= 20-char overlap), or
 (b) cites one of the card's reference IDs and that ID is not cited by the same evaluator on the unmodified base.
"""
import json, re, csv, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent
def load(p): return {json.loads(l)['id']: json.loads(l) for l in open(p, encoding='utf-8')}
cards = json.load(open(ROOT/'data/D2/cards.json', encoding='utf-8'))
norm = lambda s: re.sub(r'[\s*_`]+', ' ', s or '').strip().lower()
def ids(s): return set(re.findall(r'Q\d\.(?:[AIM]\d+|\d)', s or ''))
def overlap(frag, new):
    f, n = norm(frag), norm(new)
    if len(n) < 20 or len(f) < 20: return bool(n) and len(n) >= 8 and n in f
    return any(f[i:i+20] in n for i in range(0, len(f)-19, 5))
rows = []
for ev in ('B', 'C'):
    E = load(ROOT/f'data/eval/D2_{ev}.jsonl')
    for b in cards['bases']:
        key = b['base'][3:]
        orig = E[f'D2-{key}-ORIG']['result']['issues']
        orig_ids = set().union(*[ids(i['evidence_ref']) for i in orig]) if orig else set()
        for p in b['perturbations']:
            res = E[f'D2-{key}-{p["type"]}']['result']
            card_ids = ids(p['ref'])
            hit = None
            for i in res['issues']:
                if any(overlap(i['fragment'], new) for _, new in p['edits']):
                    hit = ('quote', i); break
            if not hit:
                for i in res['issues']:
                    new_ids = (ids(i['evidence_ref']) & card_ids) - orig_ids
                    if new_ids:
                        hit = ('ref', i); break
            rows.append({'evaluator': ev, 'object': f'D2-{key}-{p["type"]}', 'type': p['type'],
                         'expected': p['expected_detectors'], 'expected_severity': p['expected_severity'],
                         'detected': bool(hit), 'how': hit[0] if hit else '',
                         'severity': hit[1]['severity'] if hit else '', 'coarse': hit[1]['coarse_type'] if hit else '',
                         'fragment': (hit[1]['fragment'][:150] if hit else ''),
                         'material_flag': res['material_issue'], 'n_issues': len(res['issues'])})
with open(ROOT/'analysis/d2_auto_detection.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
t = collections.defaultdict(lambda: [0, 0])
for r in rows: t[(r['type'], r['evaluator'])][0] += r['detected']; t[(r['type'], r['evaluator'])][1] += 1
for ty in ('T1', 'T2', 'T3', 'T4', 'T5'):
    print(ty, 'B', '%d/%d' % tuple(t[(ty, 'B')]), 'C', '%d/%d' % tuple(t[(ty, 'C')]))
