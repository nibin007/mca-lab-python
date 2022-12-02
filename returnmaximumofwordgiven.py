def getmax(lis):
    return max(lis,key=len)

lim=int(input("enter the limit of words u want to enter"))
lis1=[]
for i in range(lim):
    lis1.append(input("enter the words--"))
print("max of the given list is in the word----", getmax(lis1))
    
