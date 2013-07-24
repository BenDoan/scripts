#!/bin/bash
#backs up a flashdrive using tar

if [ -d "/media/E018-57C9" ];
then
    filename="flashdrive_"`eval date +%Y%m%d`".tar.bz2"
    tar -jcf  /media/Backup/flashdrive/$filename /media/E018-57C9/
fi
