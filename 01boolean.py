# Name    : 01boolean

# Author  : Simon Nunn

# Date    : 03 July 2018

# Purpose : Example of boolean

number1 = float(input("Please enter first number : "))
number2 = float(input("Please enter second number: "))

if number1 > number2:
    number1bigger = True
else:
    number1bigger = False
    
print("number1 bigger:",number1bigger)

if number1bigger:
    print("number1 bigger you old git")
else:
    print("number1 not bigger youngster")






