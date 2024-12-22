num = 98
num = (str(num))

list1 = []

for x in range(len(num),-1,-1):
    list1.append(x)


data=''
for y in list1:
    data = ''.join(str(list1))
    


print(data)