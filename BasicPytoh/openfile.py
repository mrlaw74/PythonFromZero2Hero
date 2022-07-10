# Doc file: openfile.py
file = open('readme.md')
data = file.read()
print(data)
file.close()

# Ghi file: openfile.py
file1 = open('readme.md', 'a+')
file1.write('\nHello World')
data1 = file1.read()
print(data1)
file1.close()