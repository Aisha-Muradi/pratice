# pratice of OOP of 150 lectures 

class Employee:
    pass # if we say pass python would know that for now we don't want to use this otherwise it will return error 
emp1 = Employee() # this is an instance of Employee class 
emp2 = Employee() #This is another unique instance of Employee class 

print(emp1) #this is going to have a unique place in the memory when we print it 
print(emp2) #this is going to have a unique place in the memory when we print it 

#These are called the attrubiutes that are unique to each instance of a class 
emp1.first ="Ben"
emp1.last ="hum"
emp1.email ="Ben.hum@company.com"
emp1.pay = 50000

emp2.first ="Charlie"
emp2.last ="Young"
emp2.email ="Chalire.young@company.com"
emp2.pay = 10000

print(emp1, emp1.email)
print(emp2, emp2.email)


#so instead of having all these lines we can just put them into constructor __init__ so that everytime it automatically does it for us
class Employee:
    def __init__(self, first, last, pay)
    self.first = first #it does not matter for us to have it the same as the argument so I can change it to self.fname = name or anything else 
    self.last = last
    self.pay = pay 
    self.emai = first +"."+ last + "@company.com"


emp1 = Employee() # now when I call the Employee the emp1 automatically goes to self so the arguments would be like emp1.name and etc
emp2 = Employee() # same for this line 