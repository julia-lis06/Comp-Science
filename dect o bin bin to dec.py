menu = "1.Binary numbers to decimal numbers.\n2.Decimal numbers to binary numbers. \n3.Add two binary numbers"
print(menu)
choice = input("Please choose one of the given options...")
choiceint = int(choice)
print(choiceint)

#binary to decimal number
if choiceint == 1:
    urnumbinary1 = input("Enter your binary number")
    x = len(urnumbinary1) -1
    total = 0
    for i in urnumbinary1 :
        if i =="1":
            total = total + (2**x)
        else : total = total + 0
        x = x - 1
    print("In binary your decimal number is",total)
    
#decimal number to binary number
if choiceint == 2:
    urnumdec1 = input("Enter your decimal number")
    y = len(urnumdec1)
    binarylist = []
    
    
    
    
    
    
