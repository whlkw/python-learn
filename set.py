
mySet = set('this is the python set')
print(type(mySet), mySet)

list1 = [1, 2, 3, 'end']
print(set(list1))

#define set directly
set1 = {1, 2, 3, 'this is set'}
print(type(set1), 'the set1 is', set1)
set2 = set1.copy()
set2.add(6)
print(type(set2), 'the set1 by calling add is', set2)

#difference method
set3 = {1, 4, 5, 6, 'this is set'}
diff = set1.difference(set3)
print(diff)
diff2 = set1 - set3
print(diff2)

#union method
setunion = set1.union(set3)
print(setunion)

#Frozensets means that it can add items to set
#set is a immutable type
