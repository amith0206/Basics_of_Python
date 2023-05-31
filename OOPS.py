class Employee:
    salary=89000
    name="Rohan"
    def getSalary(self):
        return self.salary
rohan=Employee()
print(rohan.salary)
print(rohan.name)   

#Object creation using constructors
class Employee1:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
roshan=Employee1("Roshan",89000)
amith=Employee1("Amith",99000)
print(roshan.name) 
print(roshan.salary)       
print(amith.name)
print(amith.salary)    