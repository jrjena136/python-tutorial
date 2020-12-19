#Dictionary declaration
thisDictionary = {
    "name":"jyoti",
    "age":25,
    "profession":"Software Engineer",
    "company":"Zimbra"
}
#printin the dictionary
print(thisDictionary)
print('=========================')
#looping through all the values
for x in thisDictionary.values():
    print(x)
print('=========================')
#looping through all the keys
for x in thisDictionary.keys():
    print(x + ":",thisDictionary.get(x))
print('=========================')
#looping through keys and values
for x, y in thisDictionary.items():
    print(x, y)
print('========================')
