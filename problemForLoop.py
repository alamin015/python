#First problem. print number from -100 to -10
for x in range(-100,-9,5):
    print(x)


#problem 2: sum all the prime number lies between 1 to 1000
total =0
for x in range(2,1001):
    var=True
    for y in range(2,int(x**0.5)+1):
        if x%y==0:
            var=False
            break
    if var:
        total+=x

print(total)


