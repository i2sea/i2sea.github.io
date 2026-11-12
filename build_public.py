# 사용: python3 build_public.py overrides.json  → public/index.html (claude.ai 편집 내용을 굳혀 넣은 공개판)
import sys,json,re,os
s=open('index.html',encoding='utf8').read()
ov=json.load(open(sys.argv[1],encoding='utf8'))
ov={k:v for k,v in ov.items()}  # _page 포함
js=json.dumps(ov,ensure_ascii=False).replace("</","<\\/")
s2,n=re.subn(r"/\*BAKED\*/.*?/\*END\*/",lambda m:"/*BAKED*/"+js+"/*END*/",s,count=1,flags=re.S)
assert n==1
os.makedirs('public',exist_ok=True); open('public/index.html','w',encoding='utf8').write(s2)
print('public/index.html',len(s2))
