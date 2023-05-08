import jinja2
import os
import json
from pathlib import Path
import fnmatch
import requests
import sys

import datetime as dt
dt_India = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
Indian_time = dt_India.strftime('%d-%b-%y %H:%M:%S')

print("py file")
print(sys.argv[3])

# pagenum=1
# gitissues=[]
# while(True):
#     url=f"https://github.tools.sap/api/v3/search/issues?q=repo:kyma/service-consumption/issues?is%3Aissue+is%3Aopen+%22https%3A%2F%2Fjtrack.wdf.sap.corp%2Fbrowse%2F*%22+in%3Asummary&page={pagenum}&per_page=100"
#     headers = {
#         'Authorization': 'Bearer '+sys.argv[1],
#         'Cookie': 'logged_in=no'
#         }
#     response = requests.request("GET", url, headers=headers)
#     githubdata=response.json()
#     gitissues+= githubdata["items"]
#     if len(githubdata["items"]) < 100:
#        break
#     pagenum=pagenum+1

# def check_git_issue(serviceid: str) -> str:
#   for issue in gitissues:
#       if serviceid in str(issue):
#         return issue["html_url"]
#   return "none" 

# def getJsonFromFile(filename, externalConfigAuthMethod=None, externalConfigUserName=None, externalConfigPassword=None, externalConfigToken=None):
#     data = None
#     thisRequest = None
#     foundError = False
#     f = None

#     try:
#         # Opening JSON file
#         f = open(filename)
#         # returns JSON object as a dictionary
#         data = json.load(f)
#     except IOError:
#         message = "Can't open json file >" + filename + "<"
#         if log is not None:
#             log.error(message)
#         else:
#             print(message)
#         foundError = True
#     except ValueError as err:
#         message = "There is an issue in the json file >" + filename + \
#             "<. Issue starts on character position " + \
#             str(err.pos) + ": " + err.msg
#         if log is not None:
#             log.error(message)
#         else:
#             print(message)
#         foundError = True
#     finally:
#         if f is not None:
#             f.close()

#     if foundError is True:
#         message = "Can't run the use case before the error(s) mentioned above are not fixed"
#         if log is not None:
#             log.error(message)
#         else:
#             print(message)
#         sys.exit(os.EX_DATAERR)
#     return data

# log_files = fnmatch.filter(os.listdir("/home/user/logs/k8s/report/"),'*.log')

# content = []
# for logfile in log_files:
#   json_file=logfile.replace(".log", ".json")
#   if os.path.exists("/home/user/logs/k8s/report/"+logfile.replace(".log", ".json")):
#     with open("/home/user/logs/k8s/report/"+json_file, 'r') as f:
#       json_decoded = json.load(f)
#       if len(json_decoded) > 0:
#         if sys.argv[2] == "k8s":
#           json_decoded[0]['loglink']='https://github.tools.sap/BTP-E2EScenarioValidation/btpsatest/blob/main/logs/k8s/'+logfile
#           historylink="https://pages.github.tools.sap/BTP-E2EScenarioValidation/btpsatest/k8s/history.html"
#         else:
#           json_decoded[0]['loglink']='https://github.tools.sap/BTP-E2EScenarioValidation/btpsatest/blob/main/logs/'+logfile
#           historylink="https://pages.github.tools.sap/BTP-E2EScenarioValidation/btpsatest/history.html"
#         json_decoded[0]['githubissue']=check_git_issue(json_decoded[0]['serviceid'])
#         if json_decoded[0]['githubissue'] == "none":
#           json_decoded[0]['issuenumber']="none"
#         else:
#           x = json_decoded[0]['githubissue'].split("/")
#           json_decoded[0]['issuenumber']=x[len(x)-1]
#         source_logfile="/home/user/logs/k8s/report/"+logfile
#         with open(source_logfile, 'r') as file:
#           log_content = file.read()
#           json_decoded[0]['deleteStatus']='Failed'
#           if 'is now available' in log_content:
#             json_decoded[0]['creationStatus']='Pass'
#           else:
#             json_decoded[0]['creationStatus']='Failed'
#           if 'all service instances now deleted' in log_content:
#             json_decoded[0]['deleteStatus']='Pass'
#           if json_decoded[0]['status'] != "No API's":
#             if 'API call is successful!' in log_content:
#               json_decoded[0]['status']='Pass'
#             else:
#               json_decoded[0]['status']='Failed'
#         content += json_decoded
#       else:
#         print("SKIP : "+logfile)
#   else:
#       filename=json_file.rsplit('.', maxsplit=1)[0]
#       url=f"https://raw.githubusercontent.com/shivakumar-p12-sap/btp-auto-setup/main/use_cases/SERVICE-kyma-{filename}-use-case.json"
#       page = requests.get(url)
#       data = json.loads(page.text)
#       loglink=''
#       if sys.argv[2] == "k8s":
#         loglink='https://github.tools.sap/BTP-E2EScenarioValidation/btpsatest/blob/main/logs/k8s/'+logfile
#       else:
#         loglink='https://github.tools.sap/BTP-E2EScenarioValidation/btpsatest/blob/main/logs/'+logfile
#       githubissue=check_git_issue(data['services'][0]["api_resource_uri"]["serviceID"])
#       issuenumber=''
#       if githubissue != "none":
#         x = githubissue.split("/")
#         issuenumber=x[len(x)-1]
#       source_logfile="/home/user/logs/k8s/report/"+logfile
#       deleteStatus='Failed'
#       creationStatus='Failed'      
#       with open(source_logfile, 'r') as file:
#         log_content = file.read()
#         if 'is now available' in log_content:
#           creationStatus='Pass'
#         if 'all service instances now deleted' in log_content:
#           deleteStatus='Pass'          
#       faileddata={
#          'service': data['services'][0]['name'],
#          'plan': data['services'][0]['plan'],
#          'serviceid': data['services'][0]["api_resource_uri"]["serviceID"],
#          'status': "Failed",
#          'loglink': loglink,
#          'githubissue': githubissue,
#          'issuenumber': issuenumber,
#          'deleteStatus': deleteStatus,
#          'creationStatus': creationStatus
#         }
#       faileddatajson =json.dumps(faileddata)
#       content.append(json.loads(faileddatajson))

# passed=0
# failed=0
# for data in content:
#   if ( data['status'] == "Pass" or data['status'] == "No API's" ) and data['creationStatus'] == "Pass" and data['deleteStatus'] == "Pass":
#     passed=passed+1
#   else:
#     failed=failed+1 

# url=f"https://raw.github.tools.sap/BTP-E2EScenarioValidation/btpsatest/main/logs/history.json"
# if sys.argv[2] == "k8s":
#    url=f"https://raw.github.tools.sap/BTP-E2EScenarioValidation/btpsatest/main/logs/k8s/history.json"
# headers = {
#         'Authorization': 'Bearer '+sys.argv[1],
#         'Cookie': 'logged_in=no'
#         }
# response = requests.request("GET", url, headers=headers)
# history=response.json()

# #print(history[len(history)-1]['currentExecutionTime'])

# historyData={
# 'currentExecutionTime':Indian_time,
# 'manualTestCount':74,
# 'automatedTestCount':len(content),
# 'passedCount':passed,
# 'failedCount':failed,
# 'commitmessage':sys.argv[3]
# }  

# historyData =json.dumps(historyData)
# history.append(json.loads(historyData))

# def myFunc(e):
#   return e['service']
# content.sort(key=myFunc)
# with open('/home/user/logs/k8s/report/results.json', 'w') as f:
#     json.dump(content, f, indent=4) 

# with open('/home/user/logs/k8s/report/history.json', 'w') as f:
#     json.dump(history, f, indent=4) 

# resultInfo = getJsonFromFile('/home/user/logs/k8s/report/results.json')
# filename = '/home/user/logs/k8s/report/index.html'
# templateFilename = "/home/user/config/templates/report/index.html"
# templateFolder = os.path.dirname(templateFilename)
# templateBasename = os.path.basename(templateFilename)
# templateLoader = jinja2.FileSystemLoader(searchpath=templateFolder)
# templateEnv = jinja2.Environment(loader=templateLoader)
# template = templateEnv.get_template(templateBasename)
# with open(filename, 'w') as fh:
#     fh.write(template.render(
#         h4=Indian_time,
#         historylink=historylink,
#         names=resultInfo
#     ))

# filename = '/home/user/logs/k8s/report/history.html'
# templateFilename = "/home/user/config/templates/report/history.html"
# templateFolder = os.path.dirname(templateFilename)
# templateBasename = os.path.basename(templateFilename)
# templateLoader = jinja2.FileSystemLoader(searchpath=templateFolder)
# templateEnv = jinja2.Environment(loader=templateLoader)
# template = templateEnv.get_template(templateBasename)
# with open(filename, 'w') as fh:
#     fh.write(template.render(
#         history=reversed(history)
#     ))    