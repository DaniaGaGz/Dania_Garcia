a = ["Master", "Online"]
a.insert(1, "Code")
print (a)

b = [1,2,3,4]
c = [5,6,7,8]
c.insert(0,b)
print(c)

names = ["Sam","pelon", "DANIA"]
names.sort()
print(names)

names.sort(reverse=True)
print (names)
names.sort(reverse=True, key=len)
print(names)