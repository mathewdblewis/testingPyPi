import json, os

try:
    metaData = json.load(open('metaData.json','r'))
    assert all(e in metaData for e in ['major','minor','patch','projName'])
    projName = metaData['projName']
except Exception as e:
    projName = input("metaData.json doesn't exist, pick a project name: ")
    metaData = {'major':0,'minor':0,'patch':0,'projName':projName}

try:
    assert os.path.exists(projName) and os.path.isdir(projName)
except:
    print('project director "%s" not found' % projName)
    exit(1)

metaData['patch']+=1
verstr = str(metaData['major'])+'.'+str(metaData['minor'])+'.'+str(metaData['patch'])
json.dump(metaData,open('metaData.json','w'))



open('setup.py','w').write('metaData='+
        open('metaData.json','r').read()+\
        open('setupTemplate.py','r').read())



