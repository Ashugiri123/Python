a = 3.14
t = type(a) #class <float>

print( t )

b = "3.145"
t = type(b) #class <String>
print( t )

c = 4
t = type(c) #class <int>
print( t )

#type conversion
d = str(a)
t = type(d)
print( t )

e = float(c)
t = type(e)
print( t )

#e=int(b)#its shows error because int is smaller datatype with compare to float
# t = type()
# print( t )

#input always  take sting as a input that's why wee use typecasting
a = input();
b = input();
print(a+b)

a = int(input());
b = int(input());
print(a+b)

#use of tuple 
T=(1,);#for detecting it as a tuple you need to add a "," after your first entry
print(type(T))#tuple are immutable and it can store diffrent type of Values
