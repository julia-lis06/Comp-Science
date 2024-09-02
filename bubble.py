#bubble sort
swaps = 0
comparisons =  0
listy = []
if __name__ == "__main__":
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
        listy.append(user_input)
        #enter a new input and come back to the top of the while loop
        user_input = input("Enter a number:  ")
        #Makes sure the list is not too short and will not end the program early)
        while user_input.isalpha() and len(listy) < 3:
            print("Given input was not a number")
            user_input = input("Enter a number:  ")
        type1 = type(user_input)
    print("Error your list of numbers was to small. Please try again. (MUST BE AT LEAST 3 NUMBERS!)")
    print(listy)
    #Gets the length of list so that bubble 2 wont be out of range
    length = len(listy) -1
    #loop for different itterations of sorting
    for b in range(length):
        #moves the bubble forward every iteration
        for i in range(length):
            #gets the value of the first bubble
            Bubble1 = listy[i]
            #Gets the value second bubble
            Bubble2 = listy[i +1]
            print("Bubble1,",Bubble1 ,"Bubble2,",Bubble2)
            if Bubble1 > Bubble2:
                #switches the posistion with the value inside bubble1 with the value inside of bubble2
                listy[i] = Bubble2
                #switches the posistion with the value inside bubble2 with the value inside of bubble1
                listy[i +1] = Bubble1
                swaps = swaps + 1
            comparisons = comparisons +1
        #reduces the length of the length as the last value of the list is already sorted
        length = length - 1
        print("Amount of swaps =",swaps,"Amount of comparisons =",comparisons)
        #resetting the value of the swaps and comparisons afteer each iteration
        swaps = 0
        comparisons = 0
    print(listy)
   
   
#Simple and Intuitive Use (Line 6)
#Tolerance for Error (line 1 - line 12)