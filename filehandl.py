# opening the file in append (a) mode and add some contents on read.txt file and then read at last and then close at last
f = open("read.txt",'a')
f.write("Hello world This is about file handling.")
f.close()

f= open('read.txt','r')
print(f.read())
f.close()