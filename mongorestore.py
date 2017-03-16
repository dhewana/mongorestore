#!/usr/bin/python3

import os
import time
import datetime

DB_HOST =''
DB_PORT =''
DB_NAME = ''
BACKUP_PATH = ''

DATETIME = time.strftime('%Y%m%d-%H%M%S')
print ("DATETIME: " + DATETIME + "\n")

DATE = time.strftime('%Y%m%d')
TODAYBACKUPPATH = BACKUP_PATH + DATE + "*/" + DB_NAME + "/"

print (time.strftime('%Y%m%d-%H%M%S') + " - Starting to restore database '" + DB_NAME + "' ...")
restore_cmd = "mongorestore --host " + DB_HOST + " --port " + DB_PORT + " -d " + DB_NAME + " " + TODAYBACKUPPATH + " --gzip"
os.system(restore_cmd)
print (time.strftime('%Y%m%d-%H%M%S') + " - Restore of database '" + DB_NAME + "' completed.\n")

print (time.strftime('%Y%m%d-%H%M%S') + " - Restore script completed, your backup has been restored to " + DB_HOST + ".\n")
