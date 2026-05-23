#Adding __init__()function for child class.
class Person():
    def __init__(self,fname,lname):
        self.firstname = fname;
        self.lastname = lname;
    def Printname(abc):
        print(" My Full_name is "+abc.firstname,abc.lastname);
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
a=Student("Elon","Magar");
a.Printname();

#Adding the super() Function.
class Person():
    def __init__(self,fname,lname):
        self.firstname = fname;
        self.lastname = lname;
    def Printname(abc):
        print(" My Full_name is "+abc.firstname,abc.lastname);
class Student(Person):
    def __init__(self,fname,lname):
       super().__init__(fname,lname)
a=Student("Elon","Magar");
a.Printname();

#Adding the property for the Child class.
class Person():
    def __init__(self,fname,lname):
        self.firstname = fname;
        self.lastname = lname;
    def Printname(abc):
        print(" My Full_name is "+abc.firstname,abc.lastname);
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

        self.G_year = 2023;
a=Student("Elon","Magar");
print(a.G_year);

#Adding the method for the new child class.
class Person():
    def __init__(self,fname,lname):
        self.firstname = fname;
        self.lastname = lname;
    def Printname(abc):
        print(" My Full_name is "+abc.firstname,abc.lastname);
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        
        self.G_year=year;
    def Wow(self):
        print("Welcome ",self.firstname,self.lastname," to the class of ",self.G_year);
b=Student("Elon","Magar",2023);
b.Wow();


