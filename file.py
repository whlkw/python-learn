# open the file to write
fo = open('License.txt', 'w')
fo.write('this is a test')
print(fo.closed)
fo.close()

# create a file
fo = open('test.txt', 'w+')
fo.write('this is the first file I created via python')
fo.close()

# open the file to read
fo = open('test.txt', 'r+')
text = fo.read(10)
print(text)
fo.close()
