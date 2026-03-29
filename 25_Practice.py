class Student:

    # default constructor
    def __init__(self):
         pass
    
    # parameterized constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
    def avg(self):
            return sum(self.marks)/len(self.marks)


s1 = Student("karan",[90,80,70])
print(s1.name)
print(s1.marks)
print(s1.avg())