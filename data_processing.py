import os
import urllib
import urllib.request
import urllib.parse
from urllib.parse import unquote

with open('./data/train.csv', 'r', encoding = 'utf-8') as f:
    cnt = 0
    f.readline()
    for line in f:
        if cnt > 10:
            break
        cnt += 1
        line = line.strip().split(',')
        label = line[0]
        url = line[1].strip('\'"')
        url = unquote(url,encoding='utf-8', errors='replace') 
        idx = line[2]
        urllib.request.urlretrieve(url, './data/train/' + label[1:-1] + '_' + str(idx) + '.jpg')

