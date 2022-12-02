import subprocess

calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calcProc.poll())

print(calcProc.wait())