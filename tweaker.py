#!/usr/bin/python3


# Import part

import os
import time
import MinClick
import TopMenu
import Extend
import extra as e
import Position
import Size

# Ubuntu logo

e.logoin()

# The body of code

while 1 == 1:
    a = int (input("""
    
 ----------------------------------------
| What option do you need to manage?     |
| 1 --> Minimize on click                |
| 2 --> Menu on the top part of the dock |
| 3 --> Extended dock (fill the matter)  |
| 4 --> Change the dock alignment        |
| 5 --> Change icon size                 |
| 6 --> I want to exit                   |
 ----------------------------------------

--> """))

# Options which execute other Python files with DEFs

    if a == 1:
        MinClick.minclick()

    elif a == 2:
        TopMenu.topmenu()

    elif a == 3:
        Extend.extend()

    elif a == 4:
        Position.position()

    elif a == 5:
        Size.size()

# Exit option

    elif a == 6:
        os.system("clear")
        print("""
        
 --------------------------------------------
| We are about to exit, click ENTER to do so |
 --------------------------------------------

""")
        input()
        os.system("clear")
        break

# ERROR message

    else:
        os.system("clear")
        print("""
        
 ----------------------------------
| Try again, something went wrong! |
 ----------------------------------

""")
        input()
        os.system("clear")
        e.ubuntu(5)

e.logooff()
time.sleep(3)
os.system("clear")