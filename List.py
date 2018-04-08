
#The main properties of Python lists:'
#They are ordered'
#The contain arbitrary objects'
#Elements of a list can be accessed by an index'
#They are arbitrarily nestable, i.e. they can contain other lists as sublists'
#Variable size'
#They are mutable, i.e. the elements of a list can be changed'
myList = ['this', 'is', 'a', 'test']
print(type(myList), myList, 'its length is:', len(myList))

# list method: len and pop
myList.append(2)
myList.append('end')
print(myList)
myList.pop(0)
print(myList)

#list slice
myNewList = myList[0 : 2]
print('the sliced list is:', myNewList)

#list Concatenation
list1 = ['this', 'is', 'list', 1]
list2 = ['hello', 2, 'world']
list1 = list1 + list2
print(list1)
l3 = ['one', 'two', 3]
l3.extend(list2)
print('called extended', l3)

#list operator: in, not in

#Where is the benefit of tuples?
#Tuples are faster than lists.
#If you know that some data doesn't have to be changed, you should use tuples instead of lists,
#because this protects your data against accidental changes.
#The main advantage of tuples consists in the fact that tuples can be used as keys in dictionaries,
#while lists can't.
myTuple = (1, 'this', "a", [1, 2, 3, 'end'], 'end')
print(type(myTuple), myTuple)
print(myTuple[3][1])


