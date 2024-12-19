num1 = float(input("Insert Your Number: "))
if num1%2==0:
    print(f"{num1} is an even number")
elif num1%2!=0:
    print(f"{num1} is not an even number")


#Short hand if code
if num1>5: print("The number is greater than 5")

#Short hand if else code
print("The number is greater than 5") if num1>5 else print("The number is less than or egual of 5")