f = open("C:\\Users\\19JLison.ACC\\Documents\\Exercise.csv",'r')
j = f.readline()

print("Calories Burnt during workout")

lineslines = []
for line in f:
    line = line.strip()
    line = line.split(',')
    lineslines.append(line)
    
length = len(lineslines)
length = length - 1
print(length)

for i in range(length):
    if lineslines[i][3] == "":
        lineslines.pop(i)
        
print(lineslines)

        
        
        

#n = len(lineslines)
#for i in range(n):
 #   if lineslines[i][0] == 60:     
