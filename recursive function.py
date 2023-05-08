def factorial(num):
    if num==1:
        return 1
    else:
        return(num*factorial(num-1))
num=int(input("enter the number to find factorial:"))
if num<0:
    print("number is -ve,no factorial is possible")
elif num==0:
    print("factorial of 0 is = 1")
else:
    print("factorial=",factorial(num))
