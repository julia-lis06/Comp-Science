fin = open("C:\\Users\\19JLison.ACC\\OneDrive - Longford and Westmeath Education and Training Board\\Desktop\\New folder\\numbers.txt",'r')
total = 0
for line in fin:
   x=line.strip()
   if len(x) != 0: # if x != '':
       x = int(x)
       total = total +x
   print(total)
       
fin.close()