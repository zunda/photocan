写真缶
======

Use a Raspberry Pi to backup photographs and prepare them for upload

Preparation of Raspberry Pi
---------------------------
Photocan runs on Raspbian and usbmount package.
Git package is needed to download the photocan software.

Please install [Raspbian](https://www.raspbian.org/) into your SD card,
boot Raspberry Pi, and run
```
$ sudo apt-get install usbmount git
```

Installation and configuration of photocan
------------------------------------------
Clone the repository into the home directory and copy files into the system as folllows.

```
$ git clone https://github.com/zunda/photocan.git
$ cd photocan
$ sudo sh install.sh
```

Use
---
Follow steps below will
* Copy photos in the camera and the phone into directories ~pi/Pictures/YYYY-MM-DD with YYYY-MM-DD the date of the pictures taken on
* Copy phtoos taken on the latest date into /Download directory at the root directory of SD card in your phone

# Turn on Raspberry Pi
# Connect your camera through USB as a mass storage device
# Connect your phone through USB as a mass storage device
# Wait Raspberry Pi to power off
