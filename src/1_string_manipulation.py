
print('---repeat the string by multiply---')
print('Hi'*3)
print('*'*10)

print('---concatenation---')
text1 = 'I am'
text2 = 'here...'
print(text1 + " " + text2)
print(text1, text2)
print(f'Hi, {text1} {text2}')

print('---Index based char--')
text = 'Hello Jack'
print(text[0])
print(text[4])
print(text[-1])
print(text[-9])

#from & to range
print(text[:5])
print(text[:-3])
print(text[-3:])
print(text[4:])
print(text[6:10])
print(text[-9:-6])

print('========Built-in functions==========')
text = 'Please convert me to all uppercase/lowercase'

text_upper = text.upper()
print(text_upper)

text_lower = text.lower()
print(text_lower)

print("-----count occurrence of characters-----")
test_occ = 'Count number of u\'s in me'
print(test_occ.count('u'))

print('====Length of text=====')
text = 'What is length of this text'
print(len(text))

print("===== String string spaces on right/left side")
text = "   Strip on both side   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

text = 'abcdEfg'

print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isnumeric())

print('========for numeric=========')
text = '1234'

print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isnumeric())

print('========for string with space=========')
text = 'abd def'

print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isnumeric())