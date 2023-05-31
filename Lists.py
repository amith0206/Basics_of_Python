l1=[1,45,35,67]

print(type(l1))
print(l1)

l1.remove(67)
print(l1)

print(l1.count(35))

l1.append(87)
print(l1)

l1.extend([34,56,45])
print(l1)

print(l1.index(1))

#Gives 0th position to 3rd position
print(l1[0:4])