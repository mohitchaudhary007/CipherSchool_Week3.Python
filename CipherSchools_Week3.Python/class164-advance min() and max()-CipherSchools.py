# advabnce min() and max()

# numbers = [1,2,4,5,7]
# print(min(numbers))


names = ['Mohit Chaudhary', 'Jaat', 'ab', 'z']
print(max(names,key = lambda item : len(item)))

students = {
    'mohit' : {'score':50, 'age': 24},
    'Mohit' : {'score':75, 'age': 19},
    'mohit chaudhary' : {'score':76, 'age': 23}
}

print(max(students, key = lambda item : students[item]['age']))

# students2 = [
#     {'name':'mohit','score':90, 'age': 24},
#     {'name':'Mohit','score':70, 'age': 19},
#     {'name':'mohit chaudhary','score':60, 'age': 23},
# ]
# print(max(students2,key = lambda item:item.get('age'))['name'])