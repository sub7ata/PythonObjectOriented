print('................................. DICTIONARY ....................................')
dict = {000:'Mr./Mrs.'}
dict[100] = 'subrata'
dict[200] = 'moumita'
dict[300] = 'sun'
dict[400] = 'moon'
print(dict)

my_dict = {'name':'Subrata Das', 'age':28, 'address':'Kolkata', 'position':'Developer'}
print(my_dict)
print(my_dict['name'])

print('\n..................................... GET() ..........................................')
print(my_dict.get('age'))
print(my_dict.get('location')) # return none value
# print(my_dict['location']) # return keyerror
my_dict['age'] = 29 # update the value
print(my_dict)
my_dict['pin'] = 700001 # add new item
print(my_dict)


print('\n..................................... POP() ..........................................')
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)

print('\n................................... POPITEM() ........................................')
print(squares.popitem())
print(squares)


print('\n.................................... CLEAR() .........................................')
squares.clear()
print(squares)

print('\n.................................... del .........................................')
del squares
# print(squares) # Throws error

print('\n.................................... COPY() .........................................')
original_marks = {'Physics':67, 'Maths':87}
copied_marks = original_marks.copy() #dict.copy()
print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)

original = {1:'one', 2:'two'}
new = original.copy()
new.clear()
print('new: ', new)
print('original: ', original)


print('\n.................................... = OPERATOR .........................................')
original = {1:'one', 2:'two'}
new = original
new.clear()
print('new: ', new)
print('original: ', original)


print('\n.................................... FROMKEYS() .........................................')
keys = {'a', 'e', 'i', 'o', 'u' }
vowels = dict.fromkeys(keys)
print(vowels)

keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)

keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = dict.fromkeys(keys, value)
print(vowels)
value.append(2)
print(vowels)

keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = { key : list(value) for key in keys }
print(vowels)
value.append(2)
print(vowels)


print('\n.................................... ITEMS() .........................................')
marks = {'Physics':67, 'Maths':87}
print(marks.items())

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
items = sales.items()
print('Original items:', items)

del[sales['apple']]
print('Updated items:', items)

print('\n.................................... KEYS() .........................................')
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())

person = {'name': 'Phill', 'age': 22, }
print('Before dictionary is updated')
keys = person.keys()
print(keys)
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)