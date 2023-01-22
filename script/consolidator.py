import jinja2
import os
import json
from pathlib import Path
import fnmatch

json_files = fnmatch.filter(os.listdir("/home/user/logs/k8s/report/"),'*.json')

content = []
filenames = json_files
for filename in filenames:
    with open("/home/user/logs/k8s/report/"+filename, 'r') as f:
        content += json.load(f)
with open('/home/user/logs/k8s/report/results.json', 'w') as f:
    json.dump(content, f, indent=4)

resultInfo = getJsonFromFile('/home/user/logs/k8s/report/results.json')
filename = '/home/user/logs/k8s/report/index.html'
templateFilename = "/home/user/config/templates/report/index.html"
templateFolder = os.path.dirname(templateFilename)
templateBasename = os.path.basename(templateFilename)
templateLoader = jinja2.FileSystemLoader(searchpath=templateFolder)
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(templateBasename)
with open(filename, 'w') as fh:
    fh.write(template.render(
        h1="Cross Consumption Test Results",
        names=resultInfo
    ))
