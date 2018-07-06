# Name    : 02ifelse

# Author  : Simon Nunn

# Date    : 03 July 2018

# Purpose : Example of ifelse

mark = int(input("Enter mark: "))

if mark >= 85:
    print("Distinction")
elif mark >=75:
    print ("Merit")
elif mark >=65:
    print ("Pass")
else:
    print("Fail")
