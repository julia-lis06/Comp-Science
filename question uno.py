#question1
listlist = []
for i in range(5):
    numbers = float(input("Enter a number for the list...".format(i+1)))
    listlist.append(numbers)

print("Your original list:",listlist)

for i in range(len(listlist)):
    listlist[i] +=1
    
print("Your updated list is:",listlist) 
