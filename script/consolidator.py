import jinja2
import os
import json
from pathlib import Path
import fnmatch


def getJsonFromFile(filename, externalConfigAuthMethod=None, externalConfigUserName=None, externalConfigPassword=None, externalConfigToken=None):
    data = None
    thisRequest = None
    foundError = False
    f = None

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        message = "Can't open json file >" + filename + "<"
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    except ValueError as err:
        message = "There is an issue in the json file >" + filename + \
            "<. Issue starts on character position " + \
            str(err.pos) + ": " + err.msg
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = "Can't run the use case before the error(s) mentioned above are not fixed"
        if log is not None:
            log.error(message)
        else:
            print(message)
        sys.exit(os.EX_DATAERR)
    return data

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
    
