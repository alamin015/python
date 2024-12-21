import os
text = open('./file/hello.txt','a')
text.write(" Bangladesh is a small country.It has one million people")
text.close()


myFile =open('./file/hello.txt','r')
print(myFile.read())
myFile.close()

os.remove('./file/hello.txt')