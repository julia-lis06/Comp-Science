#mean average
num = 0
numnum = []
user_input = input("Please enter some numbers for me to put into a list...  ")
user_input_int = int(user_input)
numnum.append(user_input_int)
done = input("Are you finished adding numbers? Y/N  ")
while done != "Y":
    user_input = input("Please enter more numbers to add to the list  ")
    user_input_int = int(user_input)
    numnum.append(user_input_int)
    done = input("Are you finished adding numbers? Y/N  ")
print(numnum)
length = len(numnum)
for i in range(length):
    get = numnum[i]
    num = num + get
Mean = num / length
print("Your mean average is",Mean)
    

