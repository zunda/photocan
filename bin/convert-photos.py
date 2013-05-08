#!/usr/bin/python
import os
import glob
import time
import shutil

size=1024

mount_point = '/media/usb0/'
if os.environ.has_key('UM_MOUNTPOINT'):
	mount_point = os.environ["UM_MOUNTPOINT"].strip("\n")

ddirs = glob.glob(mount_point + '[Dd]own[Ll]oad/')
if len(ddirs) < 1:
	exit()
ddirs.sort()
ddir = ddirs[0]

pdir='/home/pi/Pictures/'
#if os.environ.has_key('HOME'):
#	pdir = os.environ["HOME"].strip("\n") + '/Pictures/'

sdirs=glob.glob(pdir + '*/')
if len(sdirs) < 1:
	exit()
sdirs.sort()
print sdirs
sdir = sdirs[-1]
print "Scanning " + sdir

date = os.path.basename(os.path.dirname(sdir))
for sfile in glob.iglob(sdir + "/*.[Jj][Pp][Gg]"):
	basename = os.path.basename(sfile)

	# Skip photos that have original in mounted device
	origfile = glob.glob(mount_point + "DCIM/*/" + basename)
	if len(origfile) > 0:
		print "Skipping " + origfile[0]
		continue

	# Destination directory
	dstdir = ddir + date + '/'
	if not os.path.isdir(dstdir):
		os.mkdir(dstdir)

	# Destination file
	dfile = dstdir + basename
	if os.path.isfile(dfile):
		print "Skipping " + dfile
		continue

	origstat = os.stat(sfile)
	cmd = "convert -resize %sx%s %s %s" % (size, size, sfile, dfile)
	print cmd
	os.system(cmd)
	os.utime(dfile, (origstat.st_atime, origstat.st_mtime))
