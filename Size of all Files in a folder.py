#! /usr/bin/python3

import os

totalSize = 0
for fileName in os.listdir('/home/saadmanfarhad/Downloads/'):
    if not os.path.isfile(os.path.join('/home/saadmanfarhad/Downloads/', fileName)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('/home/saadmanfarhad/Downloads/', fileName))
print(totalSize)
