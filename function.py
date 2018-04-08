def sayHello(name):
    'print hello to name' # this is doc string
    print("hello", name)

sayHello('world')

# int is a inmutable type, it cann't be changed in function
myInt = 10
def changeInt(myInt):
    myInt = myInt + 1
    print('the inner function value is:', myInt)

changeInt(myInt)
print('the outer int is', myInt)

# List is a muttable type, it can be changed in function
myList = [1, 2, 3, 'end']
def changeList(myList):
    myList.append(4)
    myList.pop(0)
    print('the inner function value is:', myList)

changeList(myList)
print('the outer int is', myList)

#An arbitrary parameter number can be accomplished in Python with so-called tuple references.
#An asterisk "*" is used in front of the last parameter name to denote it as a tuple reference.
def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """

    return (first + sum(values)) / (1 + len(values))

print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))

#It is also possible to pass an arbitrary number of keyword parameters to a function.
#To this purpose, we have to use the double asterisk "**"
def funcUnpacKeywordArgs(**kwargs):
    print(kwargs)
funcUnpacKeywordArgs(de="German",en="English",fr="French")
