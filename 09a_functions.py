def avg():#function defination
    a= int(input())
    b= int(input())
    c= int(input())

    average= (a+b+c)/3
    print(average)

avg()#function call
avg()#function call
avg()#function call

#python is not normally pass by reference language but in case of immutable data types it behaves like pass by value
def update(x):
    print(id(x))#prints memory address of x
    x=8
    print(id(x))#prints memory address of x after modification
    print("x:",x)#prints modified value of x


def square(number):
    return number ** 2

result = square(4)
print(result)
print("Before update function")
num = 10    
print(id(num))
update(num)
print("After update function")
print(id(num))
print("num:",num)