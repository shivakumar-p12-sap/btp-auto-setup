import sys
import json
import yaml
import pprint

print("Single script")
result=json.load(sys.argv[1])
print(result)
# f = open('add_your_service/SERVICE.json')
# data = json.load(f)
# print("JSON content")
# print(data)
# f.close()

# usecase_file=data
# def json_to_yaml(usecase_file):
#     name = usecase_file["services"][0]["name"]
#     new_name = "Test " + " ".join(list(name.split("-")))+ " service and API"
#     block_data = {
#         "name" : new_name,
#         "if":"success() || failure()",
#         "working-directory":"/home/user",
#         "shell":"bash",
#         "run": '\nkymaenv'
#     }
#     with open(".github/workflows/singleservice.yml","r") as f:
#         existing_data = yaml.safe_load(f)
#         #print(existing_data)
#     existing_data['jobs']['integration-test-kyma']['steps'].append(block_data)
#         #pprint.pprint(existing_data,sort_dicts=False)
#     #existing_data['jobs']['integration-test-kyma']['steps'].append(block_data)
#     with open('.github/workflows/singleservice.yml',"w") as k:
#         yaml.dump(existing_data,k,default_flow_style=False,sort_keys=False)

# json_to_yaml(usecase_file)