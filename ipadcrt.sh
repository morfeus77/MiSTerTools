#!/usr/bin/python3

import os
import glob
import subprocess

def backupconfig():
  ## Backup config folder first, excluding inputs subdirectory
  print("Creating a backup of your config directory...")

  exclude=['/media/fat/config/inputs','/media/fat/config/dips','/media/fat/config/nvram']
  excludeline=''

  for x in exclude:
      excludeline += ' --exclude '+x

  cmd=('tar %s -czvf /media/fat/configbackup.tar /media/fat/config' % excludeline)

  #print(cmd)

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  result=process.stdout.readlines()
  # All files were compressed
  compfiles = 0

  if len(result) >= 1:
    for line in result:
        compfiles += 1

  print("Backup created. %i files archived" % compfiles)

def installconfig():
  ## Check first if backup file exists
  if not os.path.isfile('/media/fat/configbackup.tar'):
     print("Process interrupted: backup file does not exist")
     exit()

  ## Rmove old config files
  print("Removing existing config files...")
  fileList = glob.glob('/media/fat/config/*.*')

  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

  ## Install config files from archive, removing existing config files
  print("Installing Ipad CRT config files...")
  cmd=('tar -C /media/fat -xvf /media/fat/ipadcrt.tar.gz config --no-same-owner')  

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE) 

  result=process.stdout.readlines()
  # All files were compressed
  installedfiles = 0

  if len(result) >= 1:
    for line in result:
        installedfiles += 1

  print("Installed %i config files" % installedfiles)

  ## Install alt ini file
  if os.path.isfile('/media/fat/MiSTer_alt_1.ini'):
     print("Creating backup of existing MiSTer_alt_1.ini")
     os.rename('/media/fat/MiSTer_alt_1.ini', '/media/fat/IpadCrtBackedUpAlt.ini')

  cmd=('tar -C /media/fat -xvf /media/fat/ipadcrt.tar.gz MiSTer_alt_1.ini --no-same-owner')  

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  print("Installed MiSTer_alt_1.ini")      

def restoreconfig():
  ## Restore config folder
  print("Restoring backup of your config directory...")

  ## Remove ipad crt config files
  fileList = glob.glob('/media/fat/config/*.*')

  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

  ## Restore backed up config files
  cmd=('tar -C / -xvf /media/fat/configbackup.tar')  

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  result=process.stdout.readlines()

  # All files were compressed
  restoredfiles = 0

  if len(result) >= 1:
    for line in result:
        restoredfiles += 1

  print("Restored %i config files" % restoredfiles)
  os.remove("/media/fat/configbackup.tar")

  if os.path.isfile('/media/fat/IpadCrtBackedUpAlt.ini'):
     if not os.path.isfile('MiSTer_alt_1.ini'):
       os.rename('/media/fat/IpadCrtBackedUpAlt.ini','/media/fat/MiSTer_alt_1.ini')     
       print("MiSTer_alt_1.ini restored")
     else:
       print("Could not restore MiSTer_alt_1.ini because it already exists.  Backed up version can be found as /media/fat/IpadCrtBackedUpAlt.ini")

## Check for existing backup file, if it exists offer Restore option

if os.path.isfile('/media/fat/configbackup.tar'):
  print("[1] Install Ipad CRT settings")
  print("[2] Restore old settings")
  print("Press q to quit")
  seloption = input("Please make your choice (Enter 1, 2 or q to quit):")
  if seloption == "1":
     backupconfig()
     installconfig()
  else:
     if seloption == "2":
        restoreconfig()
     else:
        if seloption.lower() == "q":
           exit()
else:
  backupconfig()
  installconfig()   

