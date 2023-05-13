#using indexing
name="Virat Kohli"
print(name[3])
print(name[0:4])
print(name[:4])
print(name[2:4])
print(name[2:])
print(name[2:10:2])
print(name[2:10:3])
print(name[-1])
print(name[-5:-2])
print(name[:-1])
print(name[-2:-5:-1]) #print in reverse
print(name[::-1]) #it reverse whole string
print(name[:-3:-1])
print(name[2:-2])
print(name[-2:2:-1])

#using slice method
x=slice(2,-2)
print(name[x])
x=slice(-2,-5,-1)
print(name[x])




