import sys
import json

print("Single script")
print(sys.argv[1])
f = open('add_your_service/SERVICE.json')
data = json.load(f)
print("JSON content")
print(data)
f.close()