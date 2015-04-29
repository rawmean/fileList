#/usr/bin/python
import os

path = '/Users/rrezaii/Documents/MyProjects/FlashFusion/FlashFusion'

fileList =[]
for filename in os.listdir(path):
	#print filename
	fileList.append(filename) 

print fileList

