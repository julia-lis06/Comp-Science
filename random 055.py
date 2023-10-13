import random
a = random.randint(1,5)
userchoice = int(input ("Choose Pick a number between 1 and 5..."))
if userchoice == a:
    print('You guessed right!')
else:
   if userchoice < a:
       print("Your guess is too low")
   else:
        print("Your guess is too high")