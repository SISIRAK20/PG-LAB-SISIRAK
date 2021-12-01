str=input("enter a string")
print("print the string:",str)
if(str.endswith("ing")):
    str=str+'ly'
else:
    str=str+'ing'
print("print new string",str)    