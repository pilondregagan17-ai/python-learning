#Types of Data type used in Python

# 1.Numeric Data Types
a = 5
print(type(a))
b = 5.0
print(type(b))
c = 2 + 4j
print(type(c))

# 2.String Data Type
s = 'Welcome to the Geeks World'
print(s)
print(type(s))
# access string with index
print(s[1])
print(s[2])
print(s[-1]) # -1 refers to the last character, -2 is second last, and so on

# 3.List Data Type
# Empty list
a = []
# list with int values
a = [1, 2, 3]
print(a)
# list with mixed values int and String
b = ["Jai", "Shree", "Ram", 4, 5]
print(b)
print("Accessing element from the list")
print(b[0])
print(b[2])
print("Accessing element using negative indexing")
print(b[-1])
print(b[-3])

# 4.
# initiate empty tuple
tup1 = ()
print("\n tuple :")
tup2 = ('Doing', 'Work')
print("\nTuple with the use of String: ", tup2)
tup3 = (1, 2, 3, 4, 5)
# access tuple items
print(tup3[0])
print(tup3[-1])
print(tup3[-3])

# 5.# initialize empty dictionary
d = {}

d = {1: 'How', 2: 'Are', 3: 'You'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'What', 2: 'Is', 3: 'Your',4: 'Name'})
print(d1)
d2 = {1: 'Gagan', 'name': 'Somraj', 3: 'Pilondre'}

# Accessing an element using key
print(d2['name'])

# Accessing a element using get
print(d2.get(1))
print(d2.get(2))
print(d2.get(3))