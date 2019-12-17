#! /usr/bin/python3

import os
for folderName, subFolders, fileNames in os.walk('/home/saadmanfarhad/Research Papers'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The file names in ' + folderName + ' are: ' + str(fileNames))
    print()
