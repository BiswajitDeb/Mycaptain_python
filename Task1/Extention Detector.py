fn= input("Enter Filename: ")

f = fn.split(".")

if f[-1]=="py":
   print("Extension of the file is : Python")
elif f[-1]=="cpp":
    e=("Extension of the file is : C++")
else: print ("Extension of the file is : " + f[-1])

