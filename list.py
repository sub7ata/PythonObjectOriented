lst = [12, 22, 25, 65, 28]
print('......................... ACCESS LIST & ELEMENTS USING INDEX .............................')
print("Original List: ", lst)
print("Length of the List: ", len(lst))
print("First Element(-ve): ", lst[-5])
print("Last Element(-ve): ", lst[-1])
print("First Element(+ve): ", lst[0])
print("Last Element(+ve): ", lst[4])


print('')
print('................................... APPEND () METHOD .......................................')
s = 'Hello World! My Name is Subrata Das'
print(s)
lst.append(s)
print(lst)
lst.append(.55)
print(lst)
lst_c = ['BlueHorse', 'NavSoft']
lst.append(lst_c)
print(lst)


print(' ')
print(".................................... EXTEND() OPERATOR ......................................")
prime = ['India', 'America (US)', 'Bangadesh']
not_prime = ['Rasia', 'Napal', 'Bhutan', 'Japan']
prime.extend(not_prime)
print('Extend List: ', prime)


print(' ')
print(".................................... EXTEND() OPERATOR ......................................")
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)
a1.extend(b)
print(a1)
a2.append(b)
print(a2)


print('')
print('........................................ STRING SPLIT .......................................')
l=[]
l.append(s)
print(l)
print(s.split("!"))
print('')

print(".................................... SLICE() OPERATOR ......................................")
list = [1,2,3,4,5,6,7,8,9,10]
print('Full List: ', list)
print("Using Slice Operator: ", list[0:len(list):1])
print("Length of the List: ", len(list))
print("Element access using Backword wise(-ve): ", list[8:2:-2])
print("Element access using Backword wise(-ve): ", list[10:0:-1])
ll1 = [9, 99, 999, 9999]
ll2 = [6, 66, 666, 6666]
ll1[len(ll1):] = ll2
print(ll1)


print(' ')
print("....................................... + OPERATOR ........................................")
l1 =[100, 200, 300]
l2 = [400, 500, 600]
list = l1 + l2
print(list)


print(' ')
print(".................................... INSERT() METHOD ......................................")
vowel = ['a', 'e', 'o', 'u']
vowel.insert(2, 'i')
print(vowel)

prime = [3, 5, 7]
prime.insert(4, 11)
print(prime)

mixed_list = [['Ram', 'Sham'], {'pin': 721445}]
tuple = (10000, 6000)
mixed_list.insert(2, tuple)
print(mixed_list)


print(' ')
print(".................................... REMOVE() METHOD ......................................")
prime_number = [3, 5, 7, 9, 11, 13]
print('Prime Number: ', prime_number)
prime_number.remove(9)
print('Updated Prime Number: ', prime_number)

prime_number = [3, 5, 7, 9, 9, 11, 13]
print('Prime Number: ', prime_number)
prime_number.remove(9)
# prime_number.remove('12') # -> Does't exists. It occurs errors.
print('Updated Prime Number: ', prime_number)

animals = ['cat', 'dog', 'rabbit', 'guinea pig']
print('Animals list: ', animals)
animals.remove('rabbit')
print('Updated animals list: ', animals)

animals = ['cat','dog', 'dog', 'rabbit', 'guinea pig']
print('Animals list: ', animals)
animals.remove('dog')
# animals.remove('cow') # -> Does't exists. It occurs errors.
print('Updated animals list: ', animals)


print(' ')
print(".................................... POP() METHOD ......................................")
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2) #list.pop(index)
print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

languages = ['Python', 'Java', 'C++', 'French', 'Ruby', 'C']
return_value = languages.pop(3)
print('\nReturn Value:', return_value)
print('Updated List:', languages)

print('\nWhen index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)

print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)


print(' ')
print(".................................... CLEAR() METHOD ......................................")
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.clear()
print('List after clear():', prime_numbers)

list = [{1, 2}, ('a'), ['1.1', '2.2']]
del list[:]
print('List:', list)


print(' ')
print(".................................... CLEAR() METHOD ......................................")
animals = ['cat', 'dog', 'rabbit', 'horse']
index = animals.index('dog') #list.index(element, start, end)
print(index)


vowels = ['a', 'e', 'i', 'o', 'i', 'u']
index = vowels.index('e')
print('The index of e:', index)
index = vowels.index('i')
print('The index of i:', index)
# index = vowels.index('p')
# print('The index of p:', index)

alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
index = alphabets.index('e')
print('The index of e:', index)
index = alphabets.index('i', 4) 
print('The index of i:', index)
# index = alphabets.index('i', 3, 5)
# print('The index of i:', index)


print(' ')
print(".................................... COUNT() METHOD ......................................")
numbers = [2, 3, 5, 2, 11, 2, 7]
count = numbers.count(2)
print('Count of 2:', count) #list.count(element)

vowels = ['a', 'e', 'i', 'o', 'i', 'u']
count = vowels.count('i')
print('The count of i is:', count)
count = vowels.count('p')
print('The count of p is:', count)

random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
count = random.count(('a', 'b'))
print("The count of ('a', 'b') is:", count)
count = random.count([3, 4])
print("The count of [3, 4] is:", count)


print(' ')
print(".................................... SORT() METHOD ......................................")
prime_numbers = [11, 3, 7, 5, 2]
prime_numbers.sort() #list.sort(key=..., reverse=...)
print("Accending Order: ", prime_numbers)
prime_numbers.sort(reverse=True)
print("Decending Order: ", prime_numbers)

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('Sorted list:', vowels)

# Sort the list in Descending order
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print('Sorted list (in Descending):', vowels)

# Sort the list using key
def takeSecond(elem):
    # print(elem[1])
    # print(elem[0])
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takeSecond)
print('Sorted list:', random)


employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

print('\n...... using the lambda function ......')
# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')


print(' ')
print(".................................... SORT() METHOD ......................................")
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()
print('Reversed List:', prime_numbers) #list.reverse()

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
systems.reverse()
print('Updated List:', systems)

# Reverse a List Using Slicing Operator
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
reversed_list = systems[::-1]
print('Updated List:', reversed_list)

# Accessing Elements in Reversed Order
systems = ['Windows', 'macOS', 'Linux']
for o in reversed(systems):
    print(o)


print("\n\n.................................... COPY() METHOD ......................................")
prime_numbers = [2, 3, 5]
numbers = prime_numbers.copy() #new_list = list.copy()
print('Copied List:', numbers)

my_list = ['cat', 0, 6.7]
new_list = my_list.copy()
print('Copied List:', new_list)

old_list = [1, 2, 3]
new_list = old_list
new_list.append('a')
print('\nNew List:', new_list)
print('Old List:', old_list)

list = ['cat', 0, 6.7]
new_list = list[:] #using slicing
new_list.append('dog')
print('\nOld List:', list)
print('New List:', new_list)