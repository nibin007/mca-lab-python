import operator
stud={}
limit=int(input("enter the total no of  student"))

for i in range(limit):
  name=input("enter the name")
  marks=int(input("enter the marks"))
  stud.update({name:marks})

sorted_d = dict(sorted(stud.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(stud.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
