f=open("text.txt","w")
seq=["firstline\n","secondline\n","thirdline\n"]
f.writelines(seq)
f.write("my first file\n")
f.write("This file\n\n")
f.write("contains three lines\n")
f=open("text.txt","r")
str=f.read()
print("read strings:",str)
f.close()
line=f.readfiles()
print("line:",file
print("file",f.name,"closed")

