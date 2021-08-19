#!/usr/bin/python3
# This script is intended to install Atrac17's Ipad CRT integer modeline
# settings on MiSTer FPGA.  Restore of original settings made possible by
# backing up existing environment during install.
import os
import glob
import subprocess

SOURCE_TAR_FILE = "/media/fat/ipadcrt.tar.gz"
BACKUP_TAR_FILE = "/media/fat/configbackup.tar"
ALT_INI_FILE = "/media/fat/MiSTer_alt_1.ini"
BACKUP_INI_FILE = "/media/fat/IpadCrtBackedUpAlt.ini"

class bcolors:
  OK = '\033[92m' #GREEN
  WARNING = '\033[93m' #YELLOW
  FAIL = '\033[91m' #RED
  RESET = '\033[0m' #RESET COLOR

def backupconfig():
  #Check if tar file can be found, if not exit
  if not os.path.isfile(SOURCE_TAR_FILE):
    print(bcolors.FAIL + ("File missing %s ... Exiting" % SOURCE_TAR_FILE) + bcolors.RESET)
    exit()

  ## Backup config folder first, excluding inputs subdirectory
  print("Creating a backup of your config directory...")

  exclude=['/media/fat/config/inputs','/media/fat/config/dips','/media/fat/config/nvram']
  excludeline=''

  for x in exclude:
      excludeline += ' --exclude '+x

  cmd=('tar %s -czvf %s /media/fat/config' % (excludeline, BACKUP_TAR_FILE))

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  result=process.stdout.readlines()
  # All files were compressed
  compfiles = 0

  if len(result) >= 1:
    for line in result:
        compfiles += 1

  print(bcolors.OK + ("Backup created. %i files archived" % compfiles) + bcolors.RESET)

def installconfig():
  ## Check first if backup file exists
  if not os.path.isfile(BACKUP_TAR_FILE):
     print(bcolors.FAIL + "Process interrupted: backup file does not exist" + bcolors.RESET)
     exit()

  ## Rmove old config files
  print("Removing existing config files...")
  fileList = glob.glob('/media/fat/config/*.*')

  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print(bcolors.FAIL + ("Error while deleting file : %s" % filePath) + bcolors.RESET)

  ## Install config files from archive, removing existing config files
  print("Extracting and installing Ipad CRT config files...")
  cmd=('tar -C /media/fat -xvf %s config --no-same-owner' % SOURCE_TAR_FILE)

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  result=process.stdout.readlines()
  # All files were compressed
  installedfiles = 0

  if len(result) >= 1:
    for line in result:
        installedfiles += 1

  print(bcolors.OK + ("Installed %i config files" % installedfiles) + bcolors.RESET)

  ## Install alt ini file
  if os.path.isfile(ALT_INI_FILE):
     print("Creating backup of existing MiSTer_alt_1.ini")
     os.replace(ALT_INI_FILE, BACKUP_INI_FILE)      

  cmd=('tar -C /media/fat -xvf %s MiSTer_alt_1.ini --no-same-owner' % SOURCE_TAR_FILE)

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  print(bcolors.OK + "Installed MiSTer_alt_1.ini" + bcolors.RESET)

def restoreconfig():
  ## Restore config folder
  print("Restoring backup of existing config files...")

  ## Remove ipad crt config files
  fileList = glob.glob('/media/fat/config/*.*')

  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print(bcolors.FAIL + ("Error while deleting file %s " % filePath) + bcolors.RESET)

  ## Restore backed up config files
  cmd=('tar -C / -xvf %s' % BACKUP_TAR_FILE)

  process = subprocess.Popen(cmd,shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  result=process.stdout.readlines()

  # All files were compressed
  restoredfiles = 0

  if len(result) >= 1:
    for line in result:
        restoredfiles += 1

  print(bcolors.OK + ("Restored %i config files" % restoredfiles) + bcolors.RESET)
  os.remove(BACKUP_TAR_FILE)

  if os.path.isfile(BACKUP_INI_FILE):
       os.rename(BACKUP_INI_FILE,ALT_INI_FILE)
       print(bcolors.OK + "Backed up MiSTer_alt_1.ini restored" + bcolors.RESET)
  else:
       print(bcolors.FAIL + "Backup of original MiSTer_alt_1.ini not found" + bcolors.RESET) 


## Check for existing backup file, if it exists offer Restore option


logo1 =r"        __                       _____________ "
logo2 =r"_____ _/  |_____________    ____/_   \______  \\"
logo3 =r"\__  \\   __\_  __ \__  \ _/ ___\|   |   /    /"
logo4 =r" / __ \|  |  |  | \// __ \\  \___|   |  /    / "
logo5 =r"(____  /__|  |__|  (____  /\___  >___| /____/  "
logo6 =r"     \/                 \/     \/              "

print(logo1)
print(logo2)
print(logo3)
print(logo4)
print(logo5)
print(logo6)

print("_________ Ipad CRT Integer Modelines __________")
print(" ")

if os.path.isfile(BACKUP_TAR_FILE):
  print("[1] Install Ipad CRT settings")
  print("[2] Restore old settings")
  print("Press q to quit")
  seloption = input("Please make your choice (Enter 1, 2 or q to quit):")
  if seloption == "1":
     print(bcolors.WARNING + "Warning! Existing backup file found.")
     print("Installing could lead to a loss of your original settings.")
     seloption = input("Are you sure you want to continue? [Y/N)? " + bcolors.RESET)
     if seloption.lower() == "y":
       backupconfig()
       installconfig()
     else:
       exit()
  else:
     if seloption == "2":
        restoreconfig()
     else:
        if seloption.lower() == "q":
           exit()
else:
  backupconfig()
  installconfig()
