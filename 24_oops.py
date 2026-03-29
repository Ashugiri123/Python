class Student:

    # default constructor
    def __init__(self):
         pass
    
    # parameterized constructor
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in Database..")

s1 = Student("karan")
print(s1.name)