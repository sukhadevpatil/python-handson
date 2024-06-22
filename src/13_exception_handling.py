
print('Handle the inputs if its not a number......')

try:
    a = int(input('Enter your age :: '))
    c = 99/a
except ValueError as exc:   #catch invalid value
    print('Age value must be numeric, please re-enter correct value.')
except ZeroDivisionError as exc:   #catch invalid value
    print('Age cannot be zero, please re-enter correct value.')
except Exception as exc:
    print('Error occurred as :: ', exc)
else:
    print(a)
    print(c)
finally:
    print('End of program...')