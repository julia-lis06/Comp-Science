#linear search
numnum =[]
#Get user input
user_input = input("Enter a number: ")
print("(to stop entering numbers please enter a letter instead)")
#if the input is a digit then continue
while user_input.isalpha():
    print("Given input was not a number")
    user_input = input("Enter a number:  ")
while user_input.isdigit() :
    user_input_int = int(user_input)
    #append the number into the list
    numnum.append(user_input)
    #enter a new input and come back to the top of the while loop
    user_input = input("Enter a number:  ")
    #Makes sure the list is not too short and will not end the program early)
while user_input.isalpha() and len(numnum) < 3:
    print("Given input was not a number")
    user_input = input("Enter a number:  ")
print(numnum)
looklook = input("Please enter the number you want to search for..")
length = len(numnum)
for i in range(length):
    a = numnum[i]
    if a == looklook:
        print("Found",looklook,"at position",i)