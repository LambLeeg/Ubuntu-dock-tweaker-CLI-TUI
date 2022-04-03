#!/usr/bin/python3

import os
import MinClick
import TopMenu
import Extend
import extra as e
import time

e.logoin()

while 1 == 1:
    a = int (input("""
    
 ----------------------------------------
| What option do you need to manage?     |
| 1 --> Minimize on click                |
| 2 --> Menu on the top part of the dock |
| 3 --> Extended dock (fill the matter)  |
| 4 --> I want to exit                   |
 ----------------------------------------

    """))

    if a == 1:
        MinClick.minclick()

    elif a == 2:
        TopMenu.topmenu()

    elif a == 3:
        Extend.extend()

    elif a == 4:
        os.system("clear")
        print("""
        
 --------------------------------------------
| We are about to exit, click ENTER to do so |
 --------------------------------------------

        """)
        input()
        os.system("clear")
        break

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
