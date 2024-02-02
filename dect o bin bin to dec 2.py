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
    urnumdec1int = int(urnumdec1)
    while urnumdec1int != 0:
        urnumdec1left = urnumdec1int % 2
        urnumdec1int = urnumdec1int // 2
        binarylist.append(urnumdec1left)
    binarylist.reverse()
    print("Your decimal number in binary is",binarylist)
    
#adding two binary numbers
if choiceint ==  3:
        print("You will be asked to enter two binary numbers you wish to add together")
        binnum1 = input("Enter your first binary number..")
        binnum2 = input("Enter your second binary number..")
        newnum = []
        r = 0
        carry = 0
        startnum = 0
        startnum2 = 0
        print(binnum1,binnum2)
        lenbinnum1 = len(binnum1)
        lenbinnum2 = len(binnum2)
        for i in range(lenbinnum1):
            startnum = startnum - 1
            variable1 = binnum1 [startnum]
            variable2 = binnum2 [startnum]
            newvari = int(variable1)+ int(variable2) + carry
            if newvari > 1:
                carry = 1
                if newvari == 2:
                    newnum.append(0)
                else: newnum.append(1)
            else:
                carry = 0
                newnum.append(newvari)
                carry = carry - carry
        if carry == 1:
            newnum.append(carry)
            newnum.reverse()
            print("Final list is", newnum)
        
        
    
    
    
    
    
    
    
    
