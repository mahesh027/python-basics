
a=(1,2.5,"virat",True)
print(a)
print(a[1])
print(a[-1])
print(a[1:3])
print(a[:-1])
b=list(a) #coverting tuple a into list using list constructor list() and storing it in b
print(b)
b.append("sachin")
print(b)
a=tuple(b) #coverting list into tuple by using tuple()
print(a)
# a.append("hi")  #can't change tuples, to change we need to convert it into list and then append and then convert to tuple and print
for i in a:
    print(i)
if "virat" in a:
    print("found")
else:
    print("not found")
print(len(a))
c=(1)  #int type
print(type(c))
c=(1,)  #tuple, if only 1 value is there then put comma otherwise it will be considered to be int type
print(type(c))
a=(1,2,3,4,5)
b=(6,8,9,10)
#a.extend(b)   //not possibe for tuple
c=a+b #concatenation
print(c)
print(c.count(6))
print(min(c))
print(max(c))
print("-------------------------------------------")

#nested tuples
d=(a,b)
print(d)
print(d[1])
print(d[0][3])
print("---------------------")
x=("kohli",)*10
print(x)
