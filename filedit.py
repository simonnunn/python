file = open("teams.txt","r")
outfile = ""
for line in range(4):
    if line % 1 == 0:
        outfile = outfile + file.readline()
    else:
        file.readline()

file = open("teams.txt","w")
file.write(outfile)
file.close()
