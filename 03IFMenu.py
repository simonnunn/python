# Name    : 05IfMenu

# Author  : Simon Nunn

# Date    : 03 July 2018

# Purpose : Example of If menu

print("Menu:")
print("1 - Add")
print("2 - Amend")
print("3 - Delete")
print("4 - Display")

menu_option = int(input("Enter Option: "))
if menu_option == 1:
    print("Option 1 - Add selected")
elif menu_option == 2:
    print("Option 2 - Amend selected")
elif menu_option == 3:
    print("Option 3 - Delete selected")
elif menu_option == 4:
    print("Option 4 - Display selected")
else:
    print("Wrong you numpty")
