
print(range(10))

print(list(range(10)))

print(type(range(10)))

print(list(range(1, 20, 2)))

print('=======================================')

x = [0, 1, 2]

for item in x:
    print(item, end = " ")
print()
print('=======================================')

for n in list(range(len(x))):
    print(x[n], end = " ")

for n in range(20):
    print(2**n, end = " ")

