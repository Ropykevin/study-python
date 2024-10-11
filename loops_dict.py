person={
    "name":"kevin",
    "age":25,
    "city":"new york"
}
# loop through items
for i ,x in person.items():
    print(i,x)
# loop through keys
for i in person.keys():
    print(i)

# loop through values 
for i in person.values():
    print(i)

# looping through 2 dictionaries using zip
person = {
    "name": "kevin",
    "age": 25,
    "city": "new york"
}

person1 = {
    "name": "arnold",
    "age": 25,
    "city": "Nairobi",
    "height":"170 cm"
}

l=[
    {
        "name": "kevin",
        "age": 25,
        "city": "new york"
    },
    {
        "name": "arnold",
        "age": 25,
        "city": "Nairobi",
    }


]
for (key,value),(key1,value1) in zip(person.items(),person1.items()):
    print(key,value,key1,value1)
