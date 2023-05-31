def greetHello():
    print("Hello")

print("Printing Hello 5 times")
i=0
for i in range(5):
    greetHello()    
    
def greetHello1(name , ending):
    print("Hello "+ name)
    print(ending)
greetHello1("Amith","Thank You")    

greetHello1("Shivam","Thanks")   

def LetterGen(name,date):
    #f string allows us to use variables inside the string
    st=f"Hi ma'am.\nThis is {name} I will be not attending class on {date}"
    print(st)
LetterGen("Amith","10th June")

def average(a,b):
    return((a+b)/2)
print(average(5,5))
    
 
        