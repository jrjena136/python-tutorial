if 5 > 2:
    print("5 is greater than 2!")

print("Hello, World!")

# This is a comment
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

print(type(35e3))

# Python Casting

# Int
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

# Float
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

# String
x = str("hello")
y = str(1)
z = str(3.2)
print(x)
print(y)
print(z)

''' 
using f-strings to replace variables

'''
first_name = "Jyotiranjan"
last_name = "Jena"
name = f"{first_name} {last_name}"
print(name)

message = 'Good Morning!!!'
print(message)
message = 'Good Night'
print(message)
print(message.title())
print(message.upper())
print(message.lower())
print(message.__len__())
