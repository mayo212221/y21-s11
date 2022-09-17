class Student:
    def __init__(self,Id,name,cgpa):
        self.Id=Id
        self.name=name
        self.cgpa=cgpa
s=Student(10,"manohar",9.3)
print(getattr(s,"name"))
setattr(s,"cgpa",10)
print(getattr(s,"cgpa"))
delattr(s,"cgpa")
print(getattr(s,"cgpa"))
print(hasattr(s,"id"))
