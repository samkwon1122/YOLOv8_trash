#!/usr/bin/bash

arr=(가구류 고철류 나무 도기류 비닐 스티로폼 유리병 의류 자전거 전자제품 종이류 캔류 페트병 플라스틱류 형광등)

mkdir -p ~/trash/labels

for i in "${arr[@]}"
do
    mkdir ~/trash/labels/"${i}"
    mv ~/trash/Validation/\[V라벨링\]라벨링데이터/"${i}"/*/*/*.txt ~/trash/labels/"${i}"/
done