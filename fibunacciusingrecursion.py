def fibo(num):
  if num<=1:
    return num 
  else:
    return(fibo(num-1)+fibo(num-2))
num=int(input("enter a positive number")
if num<=0:
        print("enter a positive integer")
else:
        print("fibonacci series-------")
        for i in range(num):
        print(fibo(i))
   
