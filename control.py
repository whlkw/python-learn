words = ['cat', 'window', 'defenestrate']

for item in words:
  print(item)

myList = list(range(5))
print(type(myList), myList)

for n in range(2, 10):
  for x in range(2, n):
      if n % x == 0:
         print(n, 'equals', x, '*', n//x)
         break
  else:
    print(n, 'is a prime')


#while loop
count = 10
while count < 100:
  if count % 10 == 0:
    print(count, 'can be devidied by 10')
  count = count + 1
