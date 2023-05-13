#higher order function - takes function as parameter or returns a function
def calm_down():
    print("calm down...")
def happy():
    print("jumping")
def sad():
    print("crying")
def feeling(fun1): #fun1=happy (address of happy)
    fun1() #now calling this fun1() will be similar to calling happy()
    return calm_down
#sad()
#happy()
print(happy)
joy=happy
joy()

print(sad)
sorrow=sad
sorrow()

msg=feeling(happy)
print(msg)
msg()