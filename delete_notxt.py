import os
from os import path

image = '/home/khc/trash/images/'
label = '/home/khc/trash/labels/'

cls = ['가구류', '고철류', '나무', '도기류', '비닐', '스티로폼', '유리병', '의류', '자전거', '전자제품', '종이류', '캔류', '페트병', '플라스틱류', '형광등']

for c in cls:
    image_c = image+c+'/'
    label_c = label+c+'/'
    for img in os.listdir(image_c):
        txt = img[:-3] + "txt"
        
        if path.exists(label_c+txt):
            continue
        else:
            os.remove(image_c+img)
    