operator = input("enter the opeerator:")
num1 = float(input("enter the 1st number 1:"))
num2 = float(input("enter the number 2:"))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)

elif operator == '*':
    result = num1 * num2
    print(result)

elif operator == '/':
    result = num1 / num2
    print(result)