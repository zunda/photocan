#!/bin/sh

ddir=$HOME/Pictures
for sdir in /media/usb?/DCIM; do
	echo Scanning $sdir
	for sfile in $sdir/*/*.JPG; do
		if [ -f $sfile ]; then
			basename=`basename $sfile`
			date=`stat -L -c %y $sfile | cut -f1 -d\ `
			datedir=$ddir/$date
			dfile=$datedir/$basename
			if [ ! -f $dfile ]; then
				if [ ! -d $datedir ]; then
					mkdir -p $datedir
				fi
				echo Copying $sfile into $datedir
				cp -p $sfile $dfile
			fi
		fi
	done
done
