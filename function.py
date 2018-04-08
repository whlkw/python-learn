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
