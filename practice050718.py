file = open("teams.txt","r")

(file.readline())
(file.readline())
print("Second and Third Character from the third team:")
(file.read(0))
(file.read(1))
print(file.read(1))
print(file.read(1))
      
file.seek(0)

print("Rest of file:")
print(file.read())

file.close()


