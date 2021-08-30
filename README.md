# MiSTerTools
Small collection of python scripts intended for use with the MiSTer project.  Custom aspect ratio calculation, modeline to video_mode conversion, video_mode to modeline conversion, ini profile switcher and a script to parse MRA files (data collection).

Online version of these tools can be found at:

https://morf77.pythonanywhere.com/vm - *Modeline to video_mode conversion*<br>

https://morf77.pythonanywhere.com/ml - *video_mode to modeline conversion*<br>

https://morf77.pythonanywhere.com/ar - *Custom aspect ratio calculation*

Custom aspect ratio calculatior is based on code by Rysha.

The webapp included in the Flask folder requires Flask-WTF and bootstrap.

https://flask-wtf.readthedocs.io/en/stable/

https://getbootstrap.com/

**Known Issues** 

Arcade cores are untested.  Cores that aren't Common Intermediate Format compliant may give wrong AR results.

## iniswitcher.sh


**iniswitcher.sh** allows you to switch between your custom ini files eg 5x.ini, 6x.ini, 15khz.ini, 31khz.ini

This script does not include ini files - you need to provide these yourself (place them in /media/fat)

![alt text](https://github.com/morfeus77/MiSTerTools/blob/main/iniswitcher.png?raw=true)

**do not edit your MiSTer.ini file itself when you use this script, instead edit your custom ini files**

Be warned this script overwrites your MiSTer.ini file.  Use the backup function if you're not sure what you're doing.
