import os

def trash():

    print("""

 --------------------------------------------------------------
| Type 1 if you need to enable a trash can icon on the desktop |
| Type 2 if you need to disable the trash icon                 |
 --------------------------------------------------------------

""")
    x = int (input("--> "))


    if x == 1:
        os.system("gsettings set org.gnome.shell.extensions.ding show-trash true")
        print ("""

 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

""")
        input()
        os.system("clear")

    elif x == 2:
        os.system("gsettings set org.gnome.shell.extensions.ding show-trash false")
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