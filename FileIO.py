s="Amith is a good boy"
#Wrting a file

with open("test.txt","w") as f:
    f.write(s)

#Reading  a file    
with open("test.txt","r") as f:
    s=f.read()
    print(s)    
  
#Appending to a file 
with open("test.txt","w") as f:
    f.write("I am writing into a file")   