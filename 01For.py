# Name    : 01For
# Author  : Simon Nunn
# Date    : 03 Jul 2018
# Purpose : Example 4*Table

timestable = int(input("Please enter number between 1 and 12: "))
if timestable >= 1 and timestable <= 12:
    for i in range(13):
        print(timestable," * ",i," = ",timestable * i)
else:timestable = int(input("Please enter number between 1 and 12: "))
if timestable >= 1 and timestable <= 12:
    for i in range(13):
        print(timestable," * ",i," = ",timestable * i)
    


