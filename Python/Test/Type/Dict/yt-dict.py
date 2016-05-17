# encoding: utf-8
# demo for showing type dict duplication
import json

js = [{"br":"Opera", "pf": "Unix"},{"br":"Firefox", "pf": "Linux"}]

cmds = [
    {"cmd":"cd /yt"},
    {"cmd":"chmod -R 775 *"},
    {"cmd":"cd jmeter-agent"},
    {"cmd":"./startAgent.sh &"}
]

cmds2 = [
    "cd /yt",
    "chmod -R 775 *",
    "cd jmeter-agent",
    "./startAgent.sh &"
]

d1=dict(name='Gumby',age=42)
print "Dict d: ",d1

items=[('name','Gumby'),('age',42)]
d2=dict(items)
print d2['name']

#ddata = json.loads(js)
print js[1]["br"]
print type(js)  # Get type
print str(js)

print "CMDs: " + cmds[1]['cmd']
print "CMDs2: " + cmds2[0]
for cmd in cmds2:
    print cmd
