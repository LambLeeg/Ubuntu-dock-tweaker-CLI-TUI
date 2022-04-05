import os

def position():

    print("""

 ------------------------------------------------
| Type 1 if you need to set dock on the BOTTOM   |
| Type 2 if you need to set dock on the LEFT     |
| Type 3 if you need to set dock on the RIGHT    |
 ------------------------------------------------

""")
    x = int (input("--> "))


    if x == 1:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM")
        print ("""

 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

""")
        input()
        os.system("clear")

    elif x == 2:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock dock-position LEFT")
        print ("""
    
 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

""")
        input()
        os.system("clear")

    elif x == 3:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock dock-position RIGHT")
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