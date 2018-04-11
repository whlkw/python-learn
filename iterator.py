
# Iterable is a class which has a method '__iter__', which returns an iterator, or a '__getitem__' method
# with sequential indexes starting with 0.

#Iterators are objects with a '__next__' method, which will be used when the function 'next' is called.

cities = ['shanghai', 'chengdu', 'beijing']
itr = iter(cities)
print(type(itr), itr)
