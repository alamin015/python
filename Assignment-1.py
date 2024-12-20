# problem 1 solution
# length = float(input('Enter the length of rect: '))
# breadth = float(input('Enter the breadth of rect: '))

# if length == breadth:
#     print("The rectangular is a square")
# else:
#     print("It is a rectangular")

# problem 2 solution
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))
num3 = float(input("Enter the third number "))
if num1>num2 and num1>num3:
    print(f"{num1} is the greatest number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest number")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is the greatest number")
else:
    print("There is no greatest value")