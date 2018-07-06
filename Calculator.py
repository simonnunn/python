# Name    : 01Calculator

# Author  : Simon Nunn

# Date    : 03 July 2018

# Purpose : Calculator

print("Menu:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Square")
print("6 - Power")


Number1 = float (input('Please enter first number: '))

Number2 = float (input('Please enter second number: '))

menu_option = int(input("Enter Option: "))
if menu_option == 1:
    print(Number1, '+ ',Number2, '=',Number1+Number2)
elif menu_option == 2:
    print(Number1, '-' ,Number2, '=',Number1-Number2)
elif menu_option == 3:
    print(Number1, '*' ,Number2, '=',Number1*Number2)
elif menu_option == 4:
    print(Number1, '/' ,Number2, '=',Number1/Number2)
elif menu_option == 5:
    print(Number1, '*' ,Number1, '=',Number1*Number1)
    print (Number2, '*' ,Number2, '=',Number2*Number2)
elif menu_option == 6:
    answer = Number1 ** Number2
    print(Number1,' ** ',Number2,' = ',answer)
else:
    print("Invalid option selected")
           



