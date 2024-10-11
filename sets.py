# its a collection of unique and unordered data
# enclosed with {}
# creating sets

my_set={1,2,3,4,5,6,7}

# set used to convert data structures into a set
# add elements into a set
my_set.add(9)
print(my_set)
# remove is used to remove elements in a set
my_set.remove(4)
print(my_set)
# membership (in)
print(60 in my_set)

# union =>used to combine all elements from both sets
x={"a","b","c","d"}
y={"e","f"}
z=x.union(y)
print(z)
# intersection =>returns elements common in both sets
a={1,2,3,4}
b={3,4,5,6}
c=a.intersection(b)
print(c)
# difference =>returns elements in the first set that are not in the second set 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = b.difference(a)
print(c)
# symmetric difference =>returns elements in either set but not in both sets 
a = {1, 2, 3, 4,5,6}
b = {3, 4, 5, 6}
c = a.symmetric_difference(b)
print(c)
days = {"monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday", "sunday", "sunday", "sunday"}
print(days)

# Remove friday and sunday from the set using methods.
# Add them back to the set
