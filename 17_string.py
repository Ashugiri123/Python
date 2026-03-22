name = input("enter your name : ")

result = name.find("o")
result1 = name.rfind("o")
print(name.index("a"))
print(result,result1)
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isalpha())#checking a name contain only alphabet or not
print(name.count("f"))
print(name.replace("f","g"))
print(name[::-1])#use to reverse a string