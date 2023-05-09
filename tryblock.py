try:
    a=10/0
except Exception as e:
    print(e)
else:
    print("a value:",a)
finally:
    print("finally executed")

#type of exception in python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
#nameerror exceptiontry:
try:
    print(a)
except NameError as e:
    print("A is not defined")
#zerodivisionerror
try:
    a=10/0
    print(a)
except ZeroDivisionError as e:
    print("divide by 0 not possible")
#valueerror
try:
    a=int("mahesh")
except ValueError as e:
    print("enter number only")
#indexerror
try:
    list=[10,20,3,8]
    print(list[10])
except IndexError as e:
    print(e)
#Filenotfounderror
try:
    f=open("mahesh.txt")
except FileNotFoundError as e:
    print(e)
else:
    print(f.read()) #create txt file mahesh and write something on it and then run program again,it will display whats inside the txt file

#handling multiple exception
try:
    a=10/2
    b=10/5
    print(b)
    c=[10,20,30,40]
    print(c[10])
except ZeroDivisionError as e:
    print("cant divide by zero")
except IndexError as e:
    print("index out of range")