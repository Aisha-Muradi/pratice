#Code based on "oop.py" file

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first #it does not matter for us to have it the same as the argument so I can change it to self.fname = name or anything else 
        self.last = last
        self.pay = pay 
        self.email = first +"."+ last + "@company.com"
        Employee.num_of_emps += 1

    def Fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # we don't need return bcz we are just going to uodate the self.pay 
        # if you are doing operation or math in the function you use return otherwise it is just going to update the value 

emp1 = Employee("Ben", "hum", 50000) 
emp2 = Employee("Charlie", "Young", 10000)
print(emp1.email)
print(emp2.email)
    
print(emp1.Fullname())
print(emp2.Fullname())
print(Employee.Fullname(emp1))

    
print(emp1.pay) 
emp1.apply_raise()
print(emp1.pay)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.__dict__)
print(Employee.num_of_emps)

print(emp1)

