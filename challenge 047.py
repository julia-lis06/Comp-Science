one = int(input ("Enter a number .."))
two = int(input ("Enter another number .."))
three = one + two
print("The total answer is", three)
f = (input("Do you want to add another number? N for no and Y for yes."))
while f == "Y":
    four = int(input ("Enter another number .."))
    p = four + three
    print("The total answer is", p)
    f = (input("Do you want to add another number? N for no and Y for yes."))

    


