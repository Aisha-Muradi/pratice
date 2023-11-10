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

emp1 = Employee("Ben", "hum", 50000) # we can put the arguments 
emp2 = Employee("Charlie", "Young", 10000)

print(emp1.email)
print(emp2.email)

print("{} {}".format(emp1.first, emp1.last)) # the format function here takes whatever we put inside the argument and puts them in order each time it sees {}

#  want to turn the print statment above into a method of this class 

    def Fullname(self): #every method always takes the instance of the class (self) otherwise it gives error
        return "{} {}".format(emp1.first, emp1.last) # instead of only returning emp1 all the time we would put self so it changes based on input
        #insteas 
        return "{} {}".format(self.first, self.last)


print(emp1.Fullname()) #we use peranthesis bcz it is a method if it was just an attribute we would not put ()

print(emp2.Fullname()) # now if we want to access another employee we simply just change the 1 to 2


# the two line below is exactly the same 
emp1.Fullname() # we assigned emp1 to Employee and then we called it / we also don't need to pass self which is instance inside the ()
Employee.Fullname(emp1) # we can directly call the class and what attrubites we want but inside the () we should put the instance we want 