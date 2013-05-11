#!/bin/sh
# install files into the system root

for dir in usr etc; do
	find $dir -type f \
		-exec echo /{} \; \
		-exec cp -p {} /{} \;
done | tee installedfiles.txt
