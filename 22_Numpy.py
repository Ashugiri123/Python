import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6],float)
print(arr.dtype)
arr = np.linspace(3, 15, 20) #creates 20 values between 3 to 15
print(arr)
arr = np.arange(1, 15, 2) #creates values from 1 to 15 with a step of 2
print(arr)
arr = np.logspace(1, 40, 5) #creates 5 values between 10^1 to 10^40
print(arr)
arr = np.zeros((3, 4)) #creates a 3x4 array of zeros    
print(arr)
arr = np.ones((4, 2)) #creates a 4x2 array of
print(arr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr = arr+2#adds 2 to each element of array
print(arr)
arr2=arr
print(id(arr2))#prints the memory address of arr2
print(id(arr))#prints the memory address of array
arr2 = arr.copy()#creates a copy of array
print(id(arr2))#prints the memory address of copy
arr2[0][0] = 100#modifies the copy
print(arr2)
print(id(arr2))#prints the memory address of copy