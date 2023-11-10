#Code based on "oop.py" file

class Employee:
    def __init__(self, first, last, pay):
        self.first = first #it does not matter for us to have it the same as the argument so I can change it to self.fname = name or anything else 
        self.last = last
        self.pay = pay 
        self.email = first +"."+ last + "@company.com"

    def Fullname(self):
        return "{} {}".format(self.first, self.last)

emp1 = Employee("Ben", "hum", 50000) 
emp2 = Employee("Charlie", "Young", 10000)
print(emp1.email)
print(emp2.email)
    
print(emp1.Fullname())
print(emp2.Fullname())
print(Employee.Fullname(emp1))
