#This is a program designed to find stored WIFI passwords on a Windows Computer. There is already a way to do this with CMD

import subprocess #Allows the python program to interface with cmd
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(["netsh", "wlan", "show", "profile", "i", "key=clear"]).decode("utf-8").split("\n")
    results = [b.split(":")[1][1:-1] for b in data if "Key Content" in b]
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))
input("")