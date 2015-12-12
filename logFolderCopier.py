#!/usr/bin/env python

'''
v0.1  2015 Dec. 12
  - add USB memory insertion recognition
  - add folder copy feature
  - add main 
'''

'''
Usage:
# sudo python logFolderCopier.py [LogFolderPath]

e.g.
# sudo python logFolderCopier.py /home/pi/linemonitor/Log/
'''


import shutil
import os.path
import sys
import time

param = sys.argv

srcpath=param[1] # xxx/Log/
dstpath="/media/pi/COPYTO"

chk1=False
chk2=False
chk3=False
while True:
	chk1 = chk2
	chk2 = chk3
	chk3 = os.path.isdir(dstpath)
	if os.path.isdir(srcpath) and os.path.isdir(dstpath):
		if chk1==False and chk2==False and chk3==True:
			print "inserted"
			shutil.copytree(srcpath, dstpath + "/Log/")
			print "Copied"
	time.sleep(0.5)


