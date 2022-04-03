import os

def topmenu():

    print("""

 ----------------------------------------------------
| Type 1 if you need to enable 'Top menu alignment'  |
| Type 2 if you need to disable this option off      |
 ----------------------------------------------------

    """)
    x = int (input("What are gonna do?... "))


    if x == 1:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top true")
        print ("""

 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

        """)
        input()
        os.system("clear")

    elif x == 2:
        os.system("gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top false")
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
