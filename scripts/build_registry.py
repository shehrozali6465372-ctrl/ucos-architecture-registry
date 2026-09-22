#!/usr/bin/env python3
from __future__ import annotations
import ast, pathlib, subprocess, sys
from datetime import datetime, timezone

if len(sys.argv) != 3: raise SystemExit('usage: build_registry.py <ucos_checkout> <registry_checkout>')
ucos = pathlib.Path(sys.argv[1]).resolve(); registry = pathlib.Path(sys.argv[2]).resolve()
out = registry / 'generated' / 'layers'; out.mkdir(parents=True, exist_ok=True); (registry / 'status').mkdir(parents=True, exist_ok=True)
def git(args): return subprocess.check_output(['git','-C',str(ucos),*args], text=True).strip()
sha = git(['rev-parse','HEAD'])
names={1:'Core',2:'Research',3:'Intelligence',4:'Writing',5:'Image',6:'Quality',7:'Publishing',8:'Analytics',9:'Learning',10:'Affiliate',11:'Integrations',12:'AI Foundation',13:'Persistence',14:'Enterprise Integration',15:'Async Runtime',16:'Database',17:'Security',18:'Monitoring',19:'Analytics Engine',20:'Image Pipeline',21:'Deployment',22:'Documentation',23:'Website Manager'}
def inventory(root):
    modules=[]; classes=[]; funcs=[]
    for p in sorted(root.rglob('*.py')):
        if any(x in {'__pycache__','.git'} for x in p.parts): continue
        rel=p.relative_to(ucos).as_posix(); modules.append(rel)
        try: tree=ast.parse(p.read_text(encoding='utf-8'), filename=rel)
        except (SyntaxError,UnicodeDecodeError): continue
        for n in ast.walk(tree):
            if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)): funcs.append(f'{rel}:{n.lineno} {n.name}()')
            elif isinstance(n,ast.ClassDef): classes.append(f'{rel}:{n.lineno} {n.name}')
    return modules,classes,funcs
for n in range(1,24):
    matches=sorted(ucos.glob(f'layers/layer{n:02d}_*')); root=matches[0] if matches else None
    modules,classes,funcs=inventory(root) if root else ([],[],[])
    lines=[f'# Layer {n:02d} — {names[n]}','',f'Implementation commit: {sha}',f'Implementation path: {root.relative_to(ucos).as_posix() if root else "NOT FOUND"}','','## Source inventory',f'- Python modules: **{len(modules)}**',f'- Classes: **{len(classes)}**',f'- Functions/methods: **{len(funcs)}**','','## Python modules']
    lines += [f'- {x}' for x in modules] or ['- None discovered.']
    lines += ['','## Classes'] + ([f'- {x}' for x in classes] or ['- None discovered.'])
    lines += ['','## Functions / methods'] + ([f'- {x}' for x in funcs] or ['- None discovered.'])
    lines += ['','## Status discipline','Generated from the implementation tree. Source presence is not live-provider or production-runtime certification.','']
    (out/f'layer-{n:02d}.md').write_text('\n'.join(lines),encoding='utf-8')
(registry/'status'/'SYNC_EVIDENCE.md').write_text(f'# Registry Sync Evidence\n\nImplementation commit scanned: {sha}\nScanned at: {datetime.now(timezone.utc).isoformat()}\n\nGenerated inventories are source-derived and do not constitute live-provider certification.\n',encoding='utf-8')
