#String and String Functions
s= "virat kohli"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("i"))
print(s.endswith("li"))
print(s.find("r")) #it returns index of r
print(s.find("i")) #'i' is present 2 times,but it returns the 1st occurence of i
print(s.find("i",2)) #it search for index of 'i' starting from 2nd index
print("-----------------------------------------------")

a="mahesh352002"
print("is upper:",a.isupper())
print("is lower:",a.islower())
print("is alphanumeric:",a.isalnum())
print("is alpha :",a.isalpha())

b="he\nis\ngood"
print(b)
print(b.splitlines()) #store in list
print(b.splitlines(True)) #store in list along with \n
a="Data is everything"
print(a.split(" "))
a=a="Data-is-everything"
print(a.split("-"))
print(a.split(" "))

s="    Mahesh     "
print(len(s))
print(len(s.strip())) #it removes unwanted spaces
print(len(s.lstrip())) #it removes unwanted spaces on left side
print(len(s.rstrip())) #it removes unwanted spaces on right side
s='12-03-2020'
print(s.partition('-'))