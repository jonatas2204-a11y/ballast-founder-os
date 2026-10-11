#!/usr/bin/env python3
import json, os, re, sys

def main(root):
    errors=[]
    pj=os.path.join(root,"plugin.json")
    if not os.path.exists(pj):errors.append("missing plugin.json")
    else:
        try:json.load(open(pj,encoding="utf-8"))
        except Exception as e:errors.append(f"invalid plugin.json: {e}")
    skills=os.path.join(root,"skills")
    count=0
    if not os.path.isdir(skills):errors.append("missing skills/")
    else:
        for name in sorted(os.listdir(skills)):
            p=os.path.join(skills,name,"SKILL.md")
            if not os.path.isfile(p):continue
            count+=1
            t=open(p,encoding="utf-8").read()
            if not t.startswith("---\n"):errors.append(f"{name}: missing frontmatter")
            if not re.search(r"\nname:\s*[^\n]+",t):errors.append(f"{name}: missing name")
            if not re.search(r"\ndescription:\s*",t):errors.append(f"{name}: missing description")
    print(f"skills: {count}")
    if errors:
        print("FAILED")
        for e in errors:print("-",e)
        return 1
    print("OK")
    return 0
if __name__=="__main__":raise SystemExit(main(sys.argv[1] if len(sys.argv)>1 else "."))
