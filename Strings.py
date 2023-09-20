b= ["Hello","world","I","need",'some','other','words',21,35.789]
First_item = b[0]
Third_item = b[2]
Num_items_in_lst = len(b)
Last_item = b[Num_items_in_lst -1]
Last_item = b[-1]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#returns items at index 2,3 and 4

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon","mango"]
print(thislist[2:]) # take everything from position 2 to the end

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:]) # print the entire list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:]) # print the entire list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #print from orange up to but not including mango

b = "Hello, World!"
print(b[2:10:2]) # return every second character starting at 2 up to but not
print(b[2:10:3]) # return every third character starting at 2 up to but not

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #prints ["a","b”,”c”,1,2,3]

b=["hello"]
output_list = b*2
print(output_list) # outputs ["hello","hello"]

My_string = 'hello'
#Make My_string uppercase and store it in a new variable:
My_string_upper = My_string.upper()
print(My_string_upper) # output is 'HELLO'
#Make My_string uppercase and store it in the old variable
My_string = My_string.upper()
print(My_string) # output is 'HELLO'

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Change more than one item at a time
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


