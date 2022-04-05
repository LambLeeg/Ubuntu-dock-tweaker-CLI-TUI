import os

def extend():

    print("""

 ------------------------------------------------
| Type 1 if you need to enable 'extended dock'   |
| Type 2 if you need to disable this option off  |
 ------------------------------------------------

""")
    x = int (input("--> "))


    if x == 1:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock extend-height true")
        print ("""

 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

""")
        input()
        os.system("clear")

    elif x == 2:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false")
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