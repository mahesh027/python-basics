user={
    "name":"mahesh",
     "age":21,
     "is married":False
    }
print(user)
print(user["name"])
     #or
print(user.get("name"))
print(user.keys())
print(user.values())
print(user.items())
print("------------------------------------")

for x in user:
    print(x)
for x in user:
    print(x," ",user[x])
print("-------------------------------------")
for x in user.values():
    print(x)
for x in user.keys():
    print(x)
for x in user.items():
    print(x)
for x,y in user.items():
    print(x,y)

#changing values

user.update({"gender":"male"})
print(user)
user["age"]=25
print(user)
user.pop("age")
print(user)
user.clear()
#del user
print(user)

#nested dictionary
user={
    "user1":{
    "name":"mahesh",
    "age":20,
     "gender":"male"
},
"user2":{
    "name":"kohli",
    "age":34,
     "gender":"male"
},
"user3":{
    "name":"dhoni",
    "age":42,
     "gender":"male"
}
}
print(user)

for x,y in user.items():
    print(x,y)