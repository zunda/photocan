#!/usr/bin/python
import os
import glob
import time
import shutil

mount_point = '/media/usb0'
if os.environ.has_key('UM_MOUNTPOINT'):
	mount_point = os.environ["UM_MOUNTPOINT"].strip("\n")

ddir='/home/pi/Pictures'
if os.environ.has_key('HOME'):
	ddir = os.environ["HOME"].strip("\n") + '/Pictures'

for sfile in glob.iglob(mount_point + "/DCIM/*/*.[Jj][Pp][Gg]"):
	basename = os.path.basename(sfile)
	date = time.strftime("%Y-%m-%d", time.gmtime(os.stat(sfile).st_mtime))
	datedir = ddir + '/' + date
	if not os.path.isdir(datedir):
		os.mkdir(datedir)
	dfile = datedir + '/' + basename
	if not os.path.isfile(dfile):
		print "Copying " + sfile + " to " + dfile
		shutil.copy2(sfile, dfile)
