#!/usr/env/bin python

'''
v0.1  2015 Dec. 12
  - add main 
'''

import shutil
import os.path
import sys

param = sys.argv

srcpath=param[1] # xxx/Log/
dstpath="/media/pi/COPYTO"
if os.path.isdir(srcpath) and os.path.isdir(dstpath):
	print "exist"
	shutil.copytree(srcpath, dstpath + "/Log/")


