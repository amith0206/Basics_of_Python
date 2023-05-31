'''Python dictionaries allow us to associate a value to a unique key, and 
then to quickly access this value'''

dict1={}
#type of the above is <class 'dict'>
print(type(dict1))

b=set()
print(type(b))
#type is <class 'set'>

dict2={"good":"Something pleasant","fetch":"to \
    bring","1":"The number is 1"}

marks={"Amith":35,"Sagar":89,"Smith":67}

print(dict2["good"])
print(marks["Amith"])

marks["Amith"]=98
print(marks)

print(marks.get("Amith"))

print(marks.keys())

print(marks.values())