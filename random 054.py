import random
choices = ["H","T"]
userchoice = (input ("Choose either H or T (heads or tails)..."))
a = random.choice(choices)
if a == userchoice:
    print("You win")
else:
    print("Bad Luck")
    



