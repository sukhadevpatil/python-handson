count = 1

while count <= 10:
    print(count)
    count = count + 1
    to_exit = input('Enter e if you wish to exit:: ')[0]
    if to_exit == 'e':
        break
print('==================================================================')

count = 0

while count <= 10:
    count = count + 1
    if count % 2:
        continue
    print(count)

print('=================For Loop============================')

for count in range(10):
    print(count + 1)

print('=================For Loop============================')

for count2 in range(2, 15):
    print(count2)

print('=================For Loop============================')

for count3 in range(2, 15, 4):
    print(count3)

print('=================For Loop============================')

for count4 in range(20, 4, -5):
    print(count4)

print('=================For Loop============================')

for count_a in range(1, 4):
    for count_b in range(1, 4):
        for count_c in range(1, 4):
            print(count_a, count_b, count_c)

print('=================For Loop============================')

students_list = ['Mary', 'John', 'Mike', 'Alice']

for std_nm in students_list:
    print(std_nm)

print('=================For Loop============================')

index = 0

while index < len(students_list):
    print(students_list[index])
    index += 1