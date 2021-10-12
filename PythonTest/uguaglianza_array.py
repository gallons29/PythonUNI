a = ["spam", "eggs", "beans"]
b = a[:]
c = a
b.append("ooo")
c.append("ppp")
print(a)
print(b)
print(c)