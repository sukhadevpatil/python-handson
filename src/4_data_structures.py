
this_is_fruits_list = ['apples', 'oranges', 'mangoes', 'pears']
print(this_is_fruits_list)
print(this_is_fruits_list[0])
print(this_is_fruits_list[1])

this_is_fruits_list[1] = 'grapes'
print(this_is_fruits_list)
print(this_is_fruits_list[1])

#right to left indexes

print(this_is_fruits_list[-1])
print(this_is_fruits_list[-2])
print(this_is_fruits_list[-3])

#mixed data type
list = ["apples", 2, 4.25, True, 'house']
print(list)
list.append(False)
print(list)

#insert values at specific index
list.insert(3, 'insert me at index 3')
print(list)

#delete value from the specific index
del list[4]
print(list)

text = 'Split me into a list'
i_am_a_list = text.split()

print(i_am_a_list)

text = ''
i_am_a_list = ['Join ', 'me ', 'into ', 'a ', 'string']

text = text.join(i_am_a_list)
print(text)