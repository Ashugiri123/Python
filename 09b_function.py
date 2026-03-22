import math
def greet(name="Guest") :
    return f"Hello, {name}!"
def multiply(p1,p2) :
    return p1 * p2
def circle_stsats(radius) :
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a,c=circle_stsats(5)
print("Area:",a)
print(f"Circumference:{c}")
print(round(c,2))


print(greet())
print(greet("Alice"))


# lamda functiomn
square = lambda x: x ** 2   #anonymous function to square a number
print(square(6))

def summ_all(*args) :#it can take any number of arguments and take them as a tuple
    print(args)
    for i in args:
        print(i)
    return sum(args)#returns the sum of all arguments
print(summ_all(1,5))  # Output: 6
print(summ_all(1,2,3,4,5))  # Output: 15


def print_kwargs(**kwargs):
 for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")
print_kwargs(product="Laptop", price=1200, brand="Dell")    
enemy="goblin"        

    
    # genrate function by using yield
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i   # yield is used to generate a value and pause the function's state

for num in even_generator(10):
    print(num)