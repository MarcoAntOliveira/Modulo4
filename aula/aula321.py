import subprocess
import sys 
cmd = ['ls', '-lah', '/']

proc = subprocess.run(
    cmd , capture_output=True,
    
)
print(proc.stdout)
#print(proc.stderr)
#print(proc.stdout.decode('cp850'))
#print(proc.returncode)
#print(sys.platform)