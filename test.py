import subprocess
x=subprocess.getoutput("ls -l| grep index | grep html | awk '{print($9)}'")
x=x.replace('\n',"")
if x=="index.html":
    print("yes")
else:
    print("no")
