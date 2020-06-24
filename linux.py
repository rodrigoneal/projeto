import subprocess

a = subprocess.getstatusoutput('route')
print(a)