# coll of data 
# enclosed with ()
# immutable
# creating tuples
# ordered
my_tuple=("lilian","kimani","grace",1000,2000)
# convert a list into a tuple you use a tuple()
x=[1,2,3,4,5]
print(x)
x=tuple(x)
print(x)
# convert a tuple into a list list()
my_tuple = ("lilian","kimani","grace",1000,2000)
# my_tuple[2] = "manfred"
my_tuple=list(my_tuple)
my_tuple[2]="manfred"
my_tuple=tuple(my_tuple)
print(my_tuple)
days = ("monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday")
# 1. Find wednesday using an index
# 2. Using a function a find the length of the tuple.
# 3. Replace Thursday with Thur
days=list(days)
days[3]="Thur"
days=tuple(days)
print(days)