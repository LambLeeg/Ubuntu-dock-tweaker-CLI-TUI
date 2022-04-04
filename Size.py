import os

def size():

    print("""

 -----------------------------------------------------
| Type 1 if you need to set icon size to 64           |
| Type 2 if you need to set icon size to 48 (DEFAULT) |
| Type 3 if you need to set icon size to 35           |
 -----------------------------------------------------

--> """)
    x = int (input("What are gonna do?... "))


    if x == 1:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 64")
        print ("""

 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

""")
        input()
        os.system("clear")

    elif x == 2:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 48")
        print ("""
    
 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

""")
        input()
        os.system("clear")

    elif x == 3:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 35")
        print ("""
    
 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

""")
        input()
        os.system("clear")

    else:
        print ("""
     
 --------------------------------------
| Hmmm... Reopen script, and try again |
| Type 1 or 2 next time (hit ENTER)    |
 --------------------------------------

""")
        input()
        os.system("clear")
pass