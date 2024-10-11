first_name="Techcamp"
second_name="Kenya"

# type function used to identify the type of 
# a variable
age=25
# print(age)
# str function is used to convert a number into
#  a numeric str
age=str(age)
# print(type(age))
# concating variables 
full_name=first_name+ " " + second_name
print(full_name)

# accessing characters in strings
# indexing
first_name = "Techcamp"
print(first_name[6])
# slicing
# extracting a substring
print(first_name[4:8])

me="i am a student at techcamp"
print(me[7:14])
print(me[7:])
# display student

# string methods 
# =>used to manipulate strings
# len =>used to find the length of a string
me = "i am a student at techcamp"
print(len(me))
# upper
me1=me.upper()
print(me1)
# lower
me2=me1.lower()
print(me2)
# strip
# -> remove leading and trailing spaces
y="     bread   ." 
stripped=y.strip()
print(len(stripped))
# replace(old,new
print(y)
replace=y.replace(" ","")
t="techcamp kenya"
# replace  kenya with africa
t=t.replace("kenya","Africa")
print(t)
# split
# 
class_main="1:2:3:4"
splits=class_main.split(":")
print(splits)
# count
t = "techcamp ccc kenya"
print(t.count("c"))

# find
print(t.find("z"))
