#Python uses a mechanism, which is known as "Call-by-Object",
#sometimes also called "Call by Object Reference" or "Call by Sharing".

#Python initially behaves like call-by-reference,
#but as soon as we are changing the value of such a variable,
#i.e. as soon as we assign a new object to it, Python "switches" to call-by-value.
#This means that a local variable x will be created and the value of the global
#variable x will be copied into it.
def ref_demo(x):
    print("x=",x," id=",id(x))
    x=42
    print("x=",x," id=",id(x))

x = 9
print(id(x))
ref_demo(x)
