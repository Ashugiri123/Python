from array import *

vals = array('i',{5,6,-7,8,9}) #it stores signed integer values
vals2= array('I',{1,2,3,4,5}) #it stores unsigned integer values
print(vals)
print(vals2)
print(vals.buffer_info()) #it shows the address and size of array
print(vals.typecode) #it shows the type of array
for i in range(len(vals)):
    print(vals[i])

for e in vals2:
    print(e)

arr= array('i',{})
n=int(input("enter the number of elements you want to add in array: "))
for i in range(n):
    x=int(input("enter the next value: "))
    arr.append(x)
print(arr)

y= int(input("enter the value to be searched: "))
k=0
for e in arr:
    if e==y:
        print(k)
        break
    k+=1