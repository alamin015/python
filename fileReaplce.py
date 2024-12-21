
data = open('./file//text.txt','r')
data = data.read()
ss = data.replace('how','now the test1')

w_data = open('./file//text.txt','w') 
w_data = w_data.write(ss)
print(w_data)