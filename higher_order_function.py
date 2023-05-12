def happy():
    print("jumping")
def sad():
    print("crying")
def feeling(fun1): #fun1=happy (address of happy)
    fun1() #now calling this fun1() will be similar to calling happy()
#sad()
#happy()
print(happy)
joy=happy
joy()

print(sad)
sorrow=sad
sorrow()

feeling(happy)