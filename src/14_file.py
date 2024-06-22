# file1 = open('my_file.txt') - this would throw an exception if file does not exists


file1 = open('my_file.txt', 'w')  # this would create new file if it's not present, if present then it overwrites

a = 'Sukhdev Patil \n'
b = 'India \n'
c = 'Software Engineer \n'

file1.write(a)
file1.write(b)
file1.write(c)

file1.close()

file2 = open('my_file.txt', 'a')  # this will append to the existing data, would not wipe out
a = 'Mary \n'
b = 'Japan \n'
c = 'Data Scientist \n'

file2.write('-------------------------\n')
file2.write(a)
file2.write(b)
file2.write(c)
file2.write('-------------------------\n')

file2.close()

file2 = open('my_file.txt', 'r')  # this will open file in read only

text = file2.read()  # reads complete content
print(text)

print('================')

file3 = open('my_file.txt', 'r')  # this will open file in read only

text1 = file3.readline()  # reads line till \n encounters
text2 = file3.readline()
text3 = file3.readline()
print(text1)
print(text2)
print(text3)

file3.close()

print('========readlines()========')

file3 = open('my_file.txt', 'r')  # this will open file in read only

text1 = file3.readlines()  # read all line in one go

print(text1)

file3.close()

print('========readlines()========')

file4 = open('my_file.txt', 'r')

text1 = file4.read(3)
print(text1)

text2 = file4.read(9)
print(text2)
print('===================================')

file5 = open('my_file.txt', 'x')  # creates new file, if file already exists then would throuw an exception

print('==============Delete file=====================')

import os

os.remove('my_file.txt')
