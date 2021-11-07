# Update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)

# 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0].update({'last_name': 'Bryant'})
# print(students)

# 3.In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# 4.Change the value 20 in z to 30
# z[0].update({'y': 30})
# print(z)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# Iterate Through a List of Dictionaries

def iterateDictionary(input):
    x = 0
    for i in students:
        print("first_name - " + str(students[x]["first_name"]) + "," " last_name - " + str(students[x]['last_name']))
        x += 1

# iterateDictionary(students)

# Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    x = 0
    for i in some_list:
        print(some_list[x][key_name])
        x += 1

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict:
        if i == 'locations':
            print("LOCATIONS")
        if i == 'instructors':
            print('INSTRUCTORS')

printInfo(dojo)