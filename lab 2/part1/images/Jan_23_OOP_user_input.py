# wearing class designer's hat
class Employee:
    # class variables with the constructor
    def __init__ (self, pName, pAge):
        self.name = pName
        self.age = pAge
    
    #name = ""
    #age = 0
    #class methods (function)
    def getBirthYear(self):
        return 2025 - self.age
    
    def calcNet(self):
        return 0
    
    
    
class PartTime(Employee):
    
    def __init__ (self, pName, pAge, pRate, pHours):
        super().__init__(pName, pAge)
        self.rate = pRate
        self.hours = pHours
    
    def calcNet(self):
        return self.rate * self.hours

class FullTime(Employee):
    
    #constructor for full time
    def __init__ (self, pName, pAge, pSalary, pBonus):
        super().__init__(pName, pAge)
        self.salary = pSalary
        self.bonus = pBonus
        
    def calcNet(self):
        return self.salary + self.bonus

class Intern(Employee):
    
    #create the constructor for Intern
    def __init__ (self, pName, pAge, pCollegeName):
        super().__init__ (pName, pAge)
        self.collegeName = pCollegeName

    def calcNet(self):
        return 1000

#################################
    
# wearing class user's hat
# create objects of classes

namept1 = input("Enter name of first parttime: ")
agept1 = int(input("Enter age of first parttime: "))
ratept1 = int(input("Enter rate of first parttime: "))
hourspt1 = int(input("Enter hours of first parttime: "))

print ("-----------------")

#e1 = PartTime("Sue",25,50,10)
e1 = PartTime(namept1,agept1,ratept1,hourspt1)


namept2 = input("Enter name of second parttime: ")
agept2 = int(input("Enter age of second parttime: "))
ratept2 = int(input("Enter rate of second parttime: "))
hourspt2 = int(input("Enter hours of second parttime: "))

#e2 = PartTime("Joe", 34, 45, 20)
e2 = PartTime(namept2,agept2,ratept2,hourspt2)

print ("-----------------")

#create ft1 with user data
ft1 = FullTime("Marc", 40, 60000, 6000)


#create ft2 with user data
ft2 = FullTime("Jessica", 32, 70000, 7000)

#create two objects Intern it1, it2

#create 2 interns with user data
it1 = Intern("Shawn", 45, "Durham College")
it2 = Intern("Paula", 30, "Lambton College")



print (f"Name: {e1.name}")
print (f"Age: {e1.age}")
earnings1 = e1.calcNet()
print (f"Net: {earnings1}")

print ("---------")
print (f"Name: {e2.name}")
print (f"Age: {e2.age}")
earnings2 = e2.calcNet()
print (f"Net: {earnings2}")



print ("---------")
print (f"Name: {ft1.name}")
print (f"Age: {ft1.age}")
earningsft1 = ft1.calcNet()
print (f"Net: {earningsft1}")

print ("---------")
print (f"Name: {ft2.name}")
print (f"Age: {ft2.age}")
earningsft2 = ft2.calcNet()
print (f"Net: {earningsft2}")

#print information about it1 and it2

print ("---------")
print (f"Name: {it1.name}")
print (f"Age: {it1.age}")
earningsit1 = it1.calcNet()
print (f"Net: {earningsit1}")
print (f"School: {it1.collegeName}")

print ("---------")
print (f"Name: {it2.name}")
print (f"Age: {it2.age}")
earningsit2 = it2.calcNet()
print (f"Net: {earningsit2}")
print (f"School: {it2.collegeName}")



birthYear1 = e1.getBirthYear()
print (f"{e1.name} you were born in {birthYear1}")

birthYear2 = e2.getBirthYear()
print (f"{e2.name} you were born in {birthYear2}")

birthYearft2 = ft2.getBirthYear()
print (f"{ft2.name} you were born in {birthYearft2}")

birthYearft1 = ft1.getBirthYear()
print (f"{ft1.name} you were born in {birthYearft1}")

birthYearit1 = it1.getBirthYear()
print (f"{it1.name} you were born in {birthYearit1}")

birthYearit2 = it2.getBirthYear()
print (f"{it2.name} you were born in {birthYearit2}")
