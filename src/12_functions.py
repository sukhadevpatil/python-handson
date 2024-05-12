x = 1


def print_me():
    global x
    x = x + 3
    print(x)


print_me()
print(x)

print('Changing global value within function is not correct way....')

x = 1


def print_me2(y):
    y = y + 3
    print(y)
    return y


x = print_me2(x)
print(x)

print('Enclosing scope -----------')


def print_me_outer():
    x = 2

    def print_me_inner():
        print(x * x)

    print_me_inner()
    print(x)


print_me_outer()

print('Built in functions......')

print(max(1, 6))


def max(a, b):
    print('user defined function .....')


print(max(1, 6))

print(help('modules'))
print(help('math'))
