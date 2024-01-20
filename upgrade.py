import os, json

prj = json.load(open('metaData.json','r'))['projName']
os.system('pip3 install --upgrade %s' % prj)

