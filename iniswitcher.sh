#!/usr/bin/python3
import sys,os
import curses
import glob
import shutil
from  curses import panel

class Menu(object):
    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
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

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL
                itemlist = item[0].split("/")
                msg = "%d. %s" % (index, itemlist[-1])
                self.window.addstr(1 + index, 1, msg, mode)

            height, width = self.window.getmaxyx()
            statusbarstr = "Press ENTER to use ini as MiSTer.ini (main)"

            if os.path.isfile('/media/fat/.activeprofile'):
               with open('/media/fat/.activeprofile', "r") as activeprofiles:
                     activeprofile = activeprofiles.readline()
            else:
               activeprofile = "Not Set"
            self.window.addstr(height-3, 1, "%s - Active profile: %s" % (statusbarstr,activeprofile))

            key = self.window.getch()
            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    break
                else:
                    activateini(self.items[self.position][0])
                    self.window.clear()
                    self.window.addstr(3 + index, 1, "Copied %s to /media/fat/MiSTer.ini" % self.items[self.position][0], mode)
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
    shutil.copyfile(inifilename, '/media/fat/MiSTer.ini')
    with open('/media/fat/.activeprofile', "w") as activeprofile:
         activeprofile.write(inifilename)

if __name__ == "__main__":
    main()

