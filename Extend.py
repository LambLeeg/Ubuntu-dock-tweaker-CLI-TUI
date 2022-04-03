import os

def extend():

    print("""

 -------------------------------------------------
| Type YES if you need to enable 'extended dock'  |
| Type NO if you need to disable this option off  |
 -------------------------------------------------

    """)
    x = input("What are gonna do?... ")


    if x == 'YES':
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock extend-height true")
        print ("""

 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

        """)
        input()
        os.system("clear")

    elif x == 'NO':
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
| Type yes or no next time (hit ENTER) |
 --------------------------------------

        """)
        input()
        os.system("clear")
pass