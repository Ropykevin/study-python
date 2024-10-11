# how to create a dictionary
person = {
    "name": "kevin",
    "age": 25,
    "location": "Kiambu"
}
# accessing values in a dictionary
print(person["name"])
# adding elements into a dictionary
person["City"] = "Nairobi"
person["units"] = ["comp", "java", "python"]
# modify
person["age"] = 30
person = {
    'name': 'kevin',
    'age': 30,
    'location': 'Kiambu',
    'City': 'Nairobi', 
    'units': ['comp', 'java', 'python'],
    "adr":{
        "code":20200,
        "str":"kimathi",
    }
    }
print(person["units"][1])#java
print(person["adr"]["str"])  # {"code": 20200,"str": "kimathi",}
person["units"].append("html")#ADD html to units
person["units"].remove("java")#remove java from units
person["adr"]["town"]="Thika"#add town adr
# update str
person["adr"]["str"]="tom"
print(person)
# dictionary methods
# .Keys  used to display all the key in a dictionary
print(person.keys())
# .valuels used to display all the values in a dictionary
print(person.values())
# .items used to display all the key value pairs 
print(person.items())
# clear
# copy
print(person.get("name"))
person.pop("name")
print(person)
