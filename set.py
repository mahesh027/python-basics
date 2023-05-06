a={'kohli','abd',18,17}
print(a)
#accessing values using for loop
for i in a:
    print(i)
b={'sachin',"dhoni",10,7}
print(b)
a.update(b)
print(a)
a.remove("sachin")
print(a)
#a.remove(15) //element 15 is not in set, so error detected
a.discard(15) #if element is present in set then it will remove it otherwise skip it,no error will be shown
print(a)
a.pop()
print(a)
#set removes duplicate data
a={"kohli","sachin",18,10,"kohli",18,1}
print(a)

#union,intersection
a={1,2,3,4,5,6}
b={6,8,1,4,18}
c=a.union(b)
print(c)
#print(a.union(b))  # or above method
print(a.intersection(b))
print(a.symmetric_difference(b)) #it gives the values otherthan the intersection values
print(a.issubset(b))
print(a.issubset(b))
print(a.issuperset(b))

