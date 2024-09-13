f = open("C:\\Users\\19JLison.ACC\\Documents\\Exercise.csv",'r')
j = f.readline()

print("Calories Burnt during workout")

list_totals_60 = 0
list_calories_60 = 0
num3_60 = 0

lineslines = []
for line in f:
    line = line.strip()
    line = line.split(',')
    lineslines.append(line)
    
length = len(lineslines)-1
print(length)

for i in range(length):
    if lineslines[i][3].strip() == "":
        continue
    else:
        o = lineslines[i][0]
        if o == "60":
            num3_60 = float(lineslines[i][3])
            list_calories_60 = list_calories_60 + num3_60
            list_totals_60 = list_totals_60 + 1
        
avg_60 = list_calories_60 / list_totals_60
avg_60 = round(avg_60,3)
print(avg_60)
            
     
print(lineslines)
