
# dictionary's key must be immutable type
firstDict = {'bob': 20, 'tom':30, 'lucy':[1, 2, 3, 4], (1,2,3): 30}
print(type(firstDict), firstDict)
print('the dictionary length is:', len(firstDict))
if 'dad' in firstDict:
  print('dad key is in dictionary')

for item in firstDict:
  print(item, firstDict[item])

# The dictionary operator is "del d[k], k in d, k not in d, len(d)"
firstDict.pop('tom')
del firstDict['lucy']
print(firstDict)

#dictionary method
copyDict = firstDict.copy()
print('the copied dictionary is: ', copyDict)

copyDict.clear()
print(copyDict)

#merge two dictionaries
newDict = {'bob': 'is a boy', (23,):45, 23.0:'this is a float'}
newDict.update(firstDict)
print('the dictionary after merged:', newDict)

#convert dictionary to list
items = newDict.items()
print(type(items), 'the dict item list is', items)
keys = newDict.keys()
print(type(keys), 'the dict keys list is', keys)
values = newDict.values()
print(type(values), 'the dict values list is', values)

#convert list to dictionay
nameList = ('tom', 'bob', 1, 6)
scoreList = ('lucy', 30, 56)
zippedData = zip(nameList, scoreList)
convertedList = list(zippedData)
createdDict = dict(convertedList)
print(type(convertedList), convertedList)
print(type(createdDict), dict(zip(nameList, scoreList)))
