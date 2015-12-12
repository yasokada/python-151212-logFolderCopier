#!/usr/env/bin python

'''
v0.1  2015 Dec. 12
  - add main 
'''

import shutil
import os.path

path1="/media/pi/COPYTO"
path2="/media/pi/CopyTo"
if os.path.isdir(path1):
	print "exist"
	shutil.copy("test.txt", path1 + "/" + "test.txt")


