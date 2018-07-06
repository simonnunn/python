# Name    : 04List

# Author  : Simon Nunn

# Date    : 03 July 2018

# Purpose : Example of List

fruit = ["Banana","Strawberry","Rasberry"]
print(fruit)
print(fruit[0])

fruit = {"Banana","Strawberry","Rasberry"}
print(fruit)
fruit.add("Goji")
print(fruit)
fruit.add("Banana")
print(fruit)

fruit = {}
fruit["Banana"] = 25
fruit["Strawberry"] = 20
fruit["Rasberry"] = 1

print(fruit)
print(fruit["Strawberry"])

if "Goji" in fruit:
    print(fruit["Rasberry"])
else:    
    print("Not specified")
