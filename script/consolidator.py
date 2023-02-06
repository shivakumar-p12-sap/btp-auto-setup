import jinja2
import os
import json
from pathlib import Path
import fnmatch

import datetime as dt
dt_India = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
Indian_time = dt_India.strftime('%d-%b-%y %H:%M:%S')


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
for filename in json_files:
    with open("/home/user/logs/k8s/report/"+filename, 'r') as f:
        json_decoded = json.load(f)
        logfile = filename.replace(".json", ".log" )
        json_decoded[0]['loglink']='https://github.tools.sap/BTP-E2EScenarioValidation/crossconsumption-report/blob/main/logs/'+logfile
        source_logfile="/home/user/logs/k8s/report/"+logfile
        with open(source_logfile, 'r') as file:
          log_content = file.read()
          json_decoded[0]['deleteStatus']='Failed'
          if 'is now available' in log_content:
            json_decoded[0]['creationStatus']='Pass'
          else:
            json_decoded[0]['creationStatus']='Failed'
          if 'all service instances now deleted' in log_content:
            json_decoded[0]['deleteStatus']='Pass'
        content += json_decoded
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
        h4=Indian_time,
        names=resultInfo
    ))
