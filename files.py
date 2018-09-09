import subprocess
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mount")
args = parser.parse_args()
dict={}
try:
    results =subprocess.check_output("sudo find "+args.mount+" -xdev -type f -printf '%p %s\t'", shell=True)
    results=results.split("\t")
    list =[]
    for i in range(results.__len__()-1):
        l=results[i]
        l=l.split(" ")
        a=[l[0],int(l[1])]
        list.append(a)    
    dict["files"]=list
except:
    dict["error"]="No such file or directory"
json_data = json.dumps(dict, sort_keys=True, indent=4)
print(json_data)
