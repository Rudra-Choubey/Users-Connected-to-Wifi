import subprocess
results = subprocess.check_output("arp -a").decode("ascii").split("\n");
for line in results:
    if "dynamic" in line:
        print(line)
