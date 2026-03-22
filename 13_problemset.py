age=int(input("enter the age:"))
# age=17
print("child" if age<18 else "adult" if age<60 else "seniorcetizen")


price= 12 if age>18 else 8
day=input("enter the day:  ")
if day=="wednesday":
    price -=2 

print(price)