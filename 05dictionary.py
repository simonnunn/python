# Name    : 05Dictionary

# Author  : Simon Nunn

# Date    : 03 July 2018

# Purpose : Example of dictionary

name = {}

name["Jack"] = 23

name["James"] = 17

name["Joe"] = 19

name["John"] = 20

print (name)

print (name["Jack"])

if "Jack" in name:
    print(name["Jack"])

else:

    print("Not in name")
