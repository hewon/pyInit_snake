'''
Created on 2014. 8. 22.

@author: csc1725
'''

import curses
stdscr = curses.initscr() # ok 시작
#curses.cbreak()         # 엔터 자동 으로 
stdscr.keypad(True)
stdscr.keypad(True)


print( stdscr.getch() )


'''
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
'''