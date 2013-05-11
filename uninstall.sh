#!/bin/sh

log=installedfiles.txt
if [ ! -e $log ]; then
	echo Install log $log is not found
	exit 1
fi
grep ^/ installedfiles.txt | xargs rm -v
rm -v installedfiles.txt
