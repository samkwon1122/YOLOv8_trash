import glob
import json
import os
from operator import itemgetter

data = '/home/khc/trash/Validation/*/*/*/*/*.Json'

cls = {'가구류':0, '고철류':1, '나무류':2, '도기류':3, '비닐류':4, '스티로폼류':5, '유리병류':6, '의류':7, '자전거':8, '전자제품':9, '종이류':10, '캔류':11, '페트병류':12, '플라스틱류':13, '형광등':14}

def is_json_key_present(js, ke):
    try:
        buf = js[ke]
    except KeyError:
        return False

    return True

for file in glob.glob(data):
    j = json.load(open(file))
    
    width = int(j['RESOLUTION'].split('*')[0])
    height = int(j['RESOLUTION'].split('*')[1])
    
    for i in range(int(j['BoundingCount'])):
        
        if not is_json_key_present(j['Bounding'][i], 'x1'):
            break
        
        a = str(cls[j['Bounding'][i]['CLASS']])
        x1 = int(j['Bounding'][i]['x1'])
        x2 = int(j['Bounding'][i]['x2'])
        y1 = int(j['Bounding'][i]['y1'])
        y2 = int(j['Bounding'][i]['y2'])

        x = str(((x1+x2) / 2)/width)
        y = str(((y1+y2) / 2)/height)
        w = str((x2 - x1)/width)
        h = str((y2 - y1)/height)
        label = a + ' ' + x + ' ' + y + ' ' + w + ' ' + h + '\n'
 
        f = open(file[:-4]+"txt", 'a')
        f.write(label)
        f.close()
    
    
    
    
    