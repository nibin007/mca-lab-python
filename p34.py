lis=[]
lim=int(input("enter the limit of student"))
for i in range(lim):
  name=input("enter the name")
  marks=int(input("enter the rollno"))
  attendance=int(input("enter the attendance"))
  student={"name":name,"rollno":marks,"attendance":attendance}
  lis.append(student)
print(lis)
