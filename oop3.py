# Creating the Child and Parent classes and Inheriting the parent class' Properties and Methods .
class Person():
    def __init__(self,fname,lname):
        self.firstname = fname;
        self.lastname = lname;
    def Printname(abc):
        print(" My Full_name is "+abc.firstname,abc.lastname);
class Student(Person):
    pass;
p1=Student("Ram","Verma")
p1.Printname();


