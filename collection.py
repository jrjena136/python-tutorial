#List operations

fruitList = ["mango", "banana", "apple"]
for x in fruitList:
    print(x)
if 'apple' in fruitList:
   print('yes, Apple is in the list')

#list length
print(len(fruitList))

#List append()
fruitList.append("orange")
print(fruitList)

#reverse list
fruitList.reverse()
print(fruitList)

#sort list
fruitList.sort()
print(fruitList)
