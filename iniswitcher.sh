#!/usr/bin/python3
import sys,os
import curses
import glob
import shutil
from  curses import panel
from datetime import datetime

class Menu(object):
    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(("Create MiSTer.ini Backup", createbackup))
        self.items.append(("Exit and reboot", "Exit"))

    def navigate(self, n):
        self.position += n

        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        ascii_art = "                  =#%+.                        .+%#-\n\
                :%@@#@@+                      +@@%@@*\n\
               -@@*.:-%@%-                  :%@%-::%@%.\n\
              -@@+.#@*.+@@+                +@@+:#@#:%@%.\n\
             =@@+.@@+@@--@@%++++++++++++++#@@-=@%+@%:%@%.\n\
          :*@@@+ -#+++** .*%%%%%%%%%%%%%%%%#. **+++#:.%@@#=\n\
         +@@*:.                                       .:+@@@-\n\
        =@@=                                              *@@:\n\
        #@@.                                              .@@+\n\
        *@@.                                              .@@+\n\
        *@@.                                              .@@+\n\
        *@@.                  +%#   .#%-                  .@@+\n\
        *@@.=*######******####@@@%**%@@@*##*******#####**:.@@+\n\
        *@@.%@+=====%@@@@@*====+@@@@@@==++=#@@@@@#=====*@#.@@+\n\
      :+@@@ #@-     .*%@%+     -@%==@@.     *%@%+      +@+.@@@+.\n\
    .*@@#=: :@@-              =@@%%%%@@=.             =@%. .=#@@+\n\
   .%@%:     :#@#:         .+%#%@%+*%@%#%*:         -%@*.     -@@#\n\
   *@@:        -#@@#+=--==*@@+:-=####=-:=%@*==--=+#@@#-        :@@*\n\
   %@#           .-+##%%%@@@+*-::=**-::-++%@@%#%#*+-.           #@%\n\
   #@%.                .#-=@%%#%%#%%#%##%%@=:#:                .%@#\n\
   :@@#.            .. *+ #-:-+%%#**#%%+-::#.-% ..            .#@@:\n\
    :#@@*-.            -.=# ..  .:--:.  .. +* -            .:*@@#:\n\
      -*@@%              :: ....      ...  .:             .@@@#-\n\
        *@@.                                              .@@+\n\
        *@@.                                              .@@+\n\
      -#@@@                                               .@@@*:\n\
     *@@*-.                     .---:.                     .:*@@+\n\
    :@@+                     :*@@@@@@@@*:                     +@@:\n\
    .@@#                    +@@*-.  .-#@@=                    +@@:\n\
     -@@@*+++++++++++++++++#@@=        =@@*+++++++++++++++++*%@@=\n\
       =#%@@@@@@@@@@@@@@@@@%%*          #%%@@@@@@@@@@@@@@@@@%#=."

        while True:
            height, width = self.window.getmaxyx()
            for y, line in enumerate(ascii_art.splitlines(), 2):
                self.window.addstr(y+8, 52, line)
            self.window.refresh()
            curses.doupdate()

            if os.path.isfile('/media/fat/.activeprofile'):
               with open('/media/fat/.activeprofile', "r") as activeprofiles:
                     activeprofile = activeprofiles.readline()
            else:
               activeprofile = "Not Set"

            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL
                itemlist = item[0].split("/")
                if item[0] == activeprofile:
                  msg = "%d. %s (currently active)" % (index, itemlist[-1])
                else:
                  msg = "%d. %s" % (index, itemlist[-1])
                self.window.addstr(1 + index, 1, msg, mode)

            statusbarstr = "ENTER to apply ini, D to delete an ini"

            self.window.addstr(height-3, 1, "%s - Active profile: %s" % (statusbarstr,activeprofile),curses.A_REVERSE)

            key = self.window.getch()
            if ((key == 100) or (key == 68)) and self.position < len(self.items) - 2:
               confirmed = deleteini(self.items[self.position][0])
               if confirmed:
                  self.items.remove(self.items[self.position])
                  self.window.clear()                
                  self.window.addstr(4 + index, 1, "%s removed" % self.items[self.position][0], mode)
               else:
                  self.window.addstr(4 + index, 1, "Delete operation cancelled", mode)
            if (key == 27):
               self.window.clear()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    break
                else:
                    if self.position == len(self.items) - 2:
                      backupfilename, overwrite  = createbackup()
                      backupname = backupfilename.split("/") 
                      if overwrite:
                        self.window.clear()
                        self.window.addstr(4 + index, 1, "MiSTer.ini backed up as %s" % backupname[-1], mode)
                        if ((backupfilename, curses.beep)) not in self.items:
                           self.items.append((backupfilename, curses.beep))
                           self.items = sorted(self.items)
                           self.window.clear()
                      else:
                        self.window.clear()
                        self.window.addstr(4 + index, 1, "Backup cancelled", mode) 
                    else:
                      activated = activateini(self.items[self.position][0])
                      if activated:
                         self.window.clear()
                         ininame = self.items[self.position][0].split("/")
                         self.window.addstr(3 + index, 1, "%s is now active..." % ininame[-1], mode)
                      else:
                         self.window.addstr(3 + index, 1, "Activation of ini cancelled")
            else:
                if key == curses.KEY_UP:
                   self.navigate(-1)
                else:
                   if key == curses.KEY_DOWN:
                      self.navigate(1)

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class IniProfileSwitcher(object):
  def __init__(self, stdscreen):
      self.screen = stdscreen
      curses.curs_set(0)
      defaultinilist = ["/media/fat/mister.ini", "/media/fat/mister_alt_1.ini", "/media/fat/mister_alt_2.ini"]
      global iniFilenamesList
      iniFilenamesList = glob.glob('/media/fat/*.ini')
      main_menu_items = []

      for inifile in iniFilenamesList:
         if inifile.lower() not in defaultinilist:
            main_menu_items.append((str(inifile),curses.beep))

      main_menu = Menu(sorted(main_menu_items), self.screen)
      main_menu.display()
      
def main():
    curses.wrapper(IniProfileSwitcher)
    curses.echo(0)
    curses.endwin()
    print("Rebooting ...")
    curses.napms(1000)
    os.system('reboot')

def activateini(inifilename):
    confirmed = throwwarning("activate")
    if confirmed:
       shutil.copyfile(inifilename, '/media/fat/MiSTer.ini')
       with open('/media/fat/.activeprofile', "w") as activeprofile:
            activeprofile.write(inifilename)
       return(True)
    else:
       return(False)

def createbackup():
    dateTimeObj = datetime.now()
    date = dateTimeObj.date()
    backupname = '/media/fat/MiSTerBackup%s.ini' % date
    if not os.path.isfile(backupname):
       shutil.copyfile('/media/fat/MiSTer.ini',backupname)
       return(backupname,True)
    else:
       overwritten = throwwarning("backup")
       if overwritten:
          shutil.copyfile('/media/fat/MiSTer.ini',backupname)
          return(backupname,True)
       else:
          return(backupname,False)

def throwwarning(type=None):
    screen = curses.initscr()
    screen.immedok(True)

    screen.border(0)

    box1 = curses.newwin(7, 50, 1, 50)
    box2 = curses.newwin(4, 45 ,2, 52)

    box1.immedok(True)
    box2.immedok(True)

    if type=="backup":
       textintro = "Warning this backup already exists"
    elif type=="activate":
       textintro = "Warning this will overwrite your MiSTer.ini"
    elif type=="delete":
       textintro = "Are you sure you want to delete this ini?"      
    actions = "\n\nPress ENTER to overwrite. ESC to cancel."
    text = textintro + actions

    box1.box()
    box2.addstr(1,0,text,curses.color_pair(2))
    key = screen.getch()

    if key in [curses.KEY_ENTER, ord("\n")]:
       screen.clear()
       return(True)
    else:
       if key == 27:
         screen.clear()
         return(False)

def deleteini(inifilename):
    confirmed = throwwarning("delete")
    if confirmed:
       os.remove(inifilename)
       return(True)
    else:
       return(False)

if __name__ == "__main__":
    main()
