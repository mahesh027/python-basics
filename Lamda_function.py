#similar concept to higher order function but named as anonymous function

add=lambda x:x+10 #it stores the address of lamda into add and while calling function add add ,it will execute...
print(add)
print(add(15))

#lambda var1,var2...varN:expression
product=lambda a,b,c:a*b*c
print(product)
print(product(4,5,6))

tall_enough=lambda h:h>175
print(tall_enough(150))

strong_enough=lambda w: "yes" if w>70 else "no"
print(strong_enough(50))


