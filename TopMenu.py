import os

def topmenu():

    print("""

 -----------------------------------------------------
| Type YES if you need to enable 'Top menu alignment' |
| Type NO if you need to disable this option off      |
 -----------------------------------------------------

    """)
    x = input("What are gonna do?... ")


    if x == 'YES' or 'Yes' or 'yes' or 'yEs' or 'yeS' or 'YEs' or 'YeS':
        os.system("""
        gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top true
        """)
        print ("""

 -----------------------------------
| All done, now check it out!       |
| Press any button (Enter) to go on |
 -----------------------------------

        """)
        input()
        os.system("clear")

    elif x == 'NO' or 'no' or 'No' or 'nO':
        os.system("""
        gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top false
        """)
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