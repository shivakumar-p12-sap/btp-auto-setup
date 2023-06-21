import sys
import json
import yaml
import pprint


import os
from pathlib import Path

print("Single script")
result=sys.argv[1]
print("JSON content")
print(result)


usecase_file=result
def json_to_yaml(usecase_file):
    print("IN function")
    current_working_directory = os.getcwd()
    print(current_working_directory)
    current_working_directory = Path.cwd()
    print(current_working_directory)
    print(os.path.abspath("history.html"))
    for usecase in usecase_file:
        print(usecase)
        with open(usecase,"r") as f:
            print(f.read())
        f.close()    
    # name = usecase_file["services"][0]["name"]
    # new_name = "Test " + " ".join(list(name.split("-")))+ " service and API"
    # block_data = {
    #     "name" : new_name,
    #     "if":"success() || failure()",
    #     "working-directory":"/home/user",
    #     "shell":"bash",
    #     "run": '\nkymaenv'
    # }
    # with open(".github/workflows/singleservice.yml","r") as f:
    #     existing_data = yaml.safe_load(f)
    #     #print(existing_data)
    # existing_data['jobs']['integration-test-kyma']['steps'].append(block_data)
    #     #pprint.pprint(existing_data,sort_dicts=False)
    # #existing_data['jobs']['integration-test-kyma']['steps'].append(block_data)
    # with open('.github/workflows/singleservice.yml',"w") as k:
    #     yaml.dump(existing_data,k,default_flow_style=False,sort_keys=False)

json_to_yaml(usecase_file)