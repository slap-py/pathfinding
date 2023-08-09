import json


f = open('output.json','r')
f = f.read()

f = json.loads(f)

print(f[list(f.keys())[0]])