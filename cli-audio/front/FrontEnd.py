import curses
import curses.textpad
from problems.Errors import CLI_Audio_Screen_Size_Exception

import sys
import os

class FrontEnd:
    """User interface class"""

    def __init__(self, player):
        """initialize the class"""

        self.player = player
        try:
            #load initial file
            self.player.play(sys.argv[1])
        except:
            #Problem loading file
            print("The file failed to load")
            pass
        else:
            #check sceen size
            t = os.get_terminal_size()        
            try: 
                if t.columns < 60 or t.lines < 20:
                    #flag sceen size too small
                    raise CLI_Audio_Screen_Size_Exception
                else:
                    #launch window
                    curses.wrapper(self.menu)
            except CLI_Audio_Screen_Size_Exception:
                print("The window is too small to run this file")
                pass
            except curses.error:
                #flags some other error from curses
                print("Curses error")
                pass
                    
    def menu(self, args):
        """Display menu sceen"""
        self.stdscr = curses.initscr()
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                #press esc to exit
                self.quit()
            elif c == ord('p'):
                self.player.pause()
                self.updateSong()
                self.stdscr.refresh()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.displaySongs()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
    
    def updateSong(self):
        """display song and pause status"""
        #clears previous status
        self.stdscr.addstr(15,10, "                                        ")
        if self.player.paused:
            self.stdscr.addstr(15,10, "Now pausing: " + self.player.getCurrentSong())
        else:
            self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self):
        """sellect song to play"""
        #points to directory containing files
        items = os.listdir("media")

        #creates list of .wav file
        fileList = []
        for names in items:
            if names.endswith(".wav"):
                fileList.append(names)

        #counts files in list
        cnt = 0
        for fileName in fileList:
            cnt = cnt + 1

        #creates pop up
        changeWindow = curses.newwin(cnt+4, 30, 5, 40)
        changeWindow.border()

        #adds file names to pop up
        cnt = 0
        for fileName in fileList:
            temp ="[{0}] {1}".format(cnt, fileName) 
            changeWindow.addstr(cnt+1,1, temp)
            cnt = cnt + 1

        #gets file sellection
        changeWindow.addstr(cnt+1,1, "File to play?")
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(cnt+1,15, 2)
        curses.noecho()
        del changeWindow
        self.stdscr.refresh()
        self.stdscr.touchwin()
        try:
            path = int(path)
        except:
            #ignore bad input
            pass
        else: 
            if path >= 0 and path < cnt:
                path = fileList[path]
                path2 ="media/"+path 
                self.player.stop()
                self.player.play(path2)

    def displaySongs(self):
        """Display list of songs"""
        #points to directory containing files
        items = os.listdir("media")

        #creates list of .wav file
        fileList = []
        for names in items:
            if names.endswith(".wav"):
                fileList.append(names)

        #counts files in list
        cnt = 0
        for fileName in fileList:
            cnt = cnt + 1

        #creates pop up
        changeWindow = curses.newwin(cnt+4, 30, 5, 40)
        changeWindow.border()

        #adds file names to pop up
        cnt = 0
        for fileName in fileList:
            temp ="[{0}] {1}".format(cnt, fileName) 
            changeWindow.addstr(cnt+1,1, temp)
            cnt = cnt + 1

        #gets file sellection
        changeWindow.addstr(cnt+1,1, "Press Enter to go back")
        self.stdscr.refresh()
        path = changeWindow.getstr(cnt+1,15, 2)
        del changeWindow
        self.stdscr.refresh()
        self.stdscr.touchwin()
        

    def quit(self):
        """Exit program"""
        self.player.stop()
        exit()
