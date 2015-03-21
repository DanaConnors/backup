#!/usr/bin/python

# allows use of the time class to use the date to name  the backup file
import datetime

# cause I was told to do this
import os
import os.path
import tarfile
import shutil

# create a variable to turn the date into a string
todayStr = datetime.date.today().isoformat()

# create the directory named with today's date if it does not already exist
if not os.path.isdir("/var/backups"):
    os.mkdir("/var/backups")
    os.mkdir("/var/backups/" + todayStr)

# parse through the backup.config file to make sure it exists
if os.path.isfile("/etc/backup.config"):

    # create a TAR file
    tarFile = tarfile.open("/var/backups/" + todayStr + ".tar.gzip", 'w:gz')

    # add files to the TAR file
    path = ("/etc/backup.config")
    if os.path.isfile(path):
        with open(path) as Files:
            for file in Files:
                tarFile.add(os.path.basename(file.rstrip()))

    # close the TAR file
    tarFile.close()
