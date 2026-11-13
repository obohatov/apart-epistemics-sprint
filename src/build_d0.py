import json, csv, sys, pathlib
root = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
M = [  # id, run, lang, model, screenshots, prompt_visible, complete, notes
 ("D0-R1-NL-GPT","1","NL","ChatGPT",["204147"],"yes","no","Single screenshot: response cut off at section 3"),
 ("D0-R1-EN-GPT","1","EN","ChatGPT",["204533","204559"],"yes","likely",""),
 ("D0-R1-EN-CL","1","EN","Claude",["204802","204833"],"yes","likely","UI model label: Sonnet 5 Medium"),
 ("D0-R1-FR-GPT","1","FR","ChatGPT",["205009","205034"],"yes","likely","Screenshots overlap"),
 ("D0-R1-FR-CL","1","FR","Claude",["205343","205422"],"partial","likely","UI model label: Sonnet 5 Medium"),
 ("D0-R1-NL-CL","1","NL","Claude",["205826","205852"],"no","likely","UI model label: Sonnet 5 Medium"),
 ("D0-R2-NL-GPT-a","2","NL","ChatGPT",["212522","212541"],"no","check","Informal 'je' address; section 5 not found in OCR"),
 ("D0-R2-FR-GPT","2","FR","ChatGPT",["212800","212821"],"no","likely",""),
 ("D0-R2-NL-CL","2","NL","Claude",["213104","213209"],"no","likely",""),
 ("D0-R2-NL-GPT-b","2","NL","ChatGPT",["213429","213502"],"no","likely","Formal 'u' address; second ChatGPT NL response in run 2 — possibly the re-collected response"),
 ("D0-R2-EN-CL","2","EN","Claude",["213638","213707"],"no","likely","UI model label: Sonnet 5 Medium"),
 ("D0-R2-FR-CL","2","FR","Claude",["213914","213936"],"no","likely","UI model label: Sonnet 5 Medium"),
 ("D0-R2-EN-GPT","2","EN","ChatGPT",["214112","214133"],"no","likely",""),
 ("D0-R3-EN-GPT","3","EN","ChatGPT",["215404","215553"],"no","likely",""),
 ("D0-R3-NL-CL","3","NL","Claude",["220011","220033"],"no","likely",""),
 ("D0-R3-EN-CL","3","EN","Claude",["220220","220247"],"no","likely",""),
 ("D0-R3-NL-GPT","3","NL","ChatGPT",["220427","220446"],"no","likely",""),
 ("D0-R3-FR-CL","3","FR","Claude",["220656","220718"],"no","likely",""),
 ("D0-R3-FR-GPT","3","FR","ChatGPT",["220814","220839"],"no","check","End of second screenshot incomplete"),
]
used=set(); rows=[]
with open(out/"d0_responses_raw.jsonl","w",encoding="utf-8") as js:
  for i,run,lang,model,shots,pv,comp,notes in M:
    texts=[]
    for s in shots:
      p=root/"ocr"/f"run{run}_{s}.txt"; used.add(p.name)
      texts.append(p.read_text(encoding="utf-8"))
    files=[f"run{run}/Screenshot 2026-07-30 {s}.png" for s in shots]
    js.write(json.dumps({"id":i,"run":int(run),"language":lang,"system":model,
      "collected":"2026-07-30","screenshots":files,"prompt_visible":pv,"completeness":comp,
      "text_source":"OCR (tesseract eng+fra+nld), uncleaned; screenshots may overlap",
      "citations":"chip labels only, URLs not recoverable from screenshots",
      "notes":notes,"text_raw":"\n\n----- next screenshot -----\n\n".join(texts)},ensure_ascii=False)+"\n")
    rows.append([i,run,lang,model,len(shots),pv,comp,notes])
with open(out/"d0_inventory.csv","w",newline="",encoding="utf-8") as f:
  w=csv.writer(f); w.writerow(["id","run","language","system","screenshots","prompt_visible","completeness","notes"]); w.writerows(rows)
allf={p.name for p in (root/"ocr").glob("*.txt")}
print("unassigned:",sorted(allf-used)); print(len(rows),"responses")
