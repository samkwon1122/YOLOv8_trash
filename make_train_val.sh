#!/usr/bin/bash

arr=(가구류 고철류 나무 도기류 비닐 스티로폼 유리병 의류 자전거 전자제품 종이류 캔류 페트병 플라스틱류 형광등)

mkdir -p ~/trash/train_100/images
mkdir ~/trash/train_100/labels
mkdir -p ~/trash/val_100/images
mkdir ~/trash/val_100/labels

for i in "${arr[@]}"
do
    mv ~/trash/images_100/train/"${i}"/*.jpg ~/trash/train_100/images/
    mv ~/trash/labels_100/train/"${i}"/*.txt ~/trash/train_100/labels/
    mv ~/trash/images_100/val/"${i}"/*.jpg ~/trash/val_100/images/
    mv ~/trash/labels_100/val/"${i}"/*.txt ~/trash/val_100/labels/
done

#rm -rf ~/trash/images_100
#rm -rf ~/trash/labels_100