#!/usr/bin/python3
import sys,os
import curses
import glob
from  curses import panel

class Menu(object):
    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.video_mode = None
        self.items = items
        self.items.append(("Exit", "exit"))


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

                    msg = "%d. %s" % (index, item[0])

                    self.window.addstr(1 + index, 1, msg, mode)

                key = self.window.getch()

                if key in [curses.KEY_ENTER, ord("\n")]:
                    if self.position == len(self.items) - 1:
                        break
                    else:
                        self.items[self.position][1]()
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
      iniFilenamesList = glob.glob('*.ini')
      main_menu_items = []
      for inifile in iniFilenamesList:
         main_menu_items.append((str(inifile),curses.beep))
      main_menu = Menu(main_menu_items, self.screen)
      main_menu.display()


def main():
    curses.wrapper(IniProfileSwitcher)

if __name__ == "__main__":
                main()
