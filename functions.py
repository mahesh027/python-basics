def welcome():
    print("hello")
welcome()
welcome()

def num():
    pass
print(type(num))

#1. No return type without argument function
def add():
    a=int(input("enter num1:"))
    b=int(input("enter num2:"))
    c=a+b
    print("sum is",c)
add()

#2.No return type with argument function
def sub(a,b):
    c=a-b
    print("difference:",c)
sub(25,10)

#3.Return type without argument
def mul():
    a = int(input("enter num1:"))
    b = int(input("enter num2:"))
    c = a * b
    return c
result=mul()
print("result=",result)

#4.Return type with argument
def div(a,b):
    c=a/b
    return c
result=div(25,5)
print("result:",result)



#5.arbitrary arguments funcion (*) // * can be used to pass more than 2 arguments by converting it into tuple
def class_10(*students):
    print(students)
    print(students[2])
    for x in students:
        print(x)
class_10('mahesh',"kohli",'sachin',18,20)

#6.keyword argument function
def user(name,age):
    print(name,"age is",age)
user(age=20,name="mahesh")

#7.arbitrary keyword arguments (**) //will convert to dictionary
def user(**data):
    print(data)
    print(data["name"])
    print(data.values())
    print(data.items())
    for x,y in data.items():
        print(x,y)
user(name="mahesh",age=25,gender="male")

#8.default parameter function
def user(name,city="kaloor"):
    print(name,"lives in",city)
user("virat","ernakulam")
user("mahesh")

#9.passing list as an argument
def total(marks):
    return sum(marks)
print(total([10,20,55,60,88]))




