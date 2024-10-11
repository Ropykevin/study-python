# create a list
fruits=["apple","oranges","mangoes","bananas"]
print(fruits[-1])

# TASK: Create a List of days of the Week. 
# Print the day today using an index.
days_of_week=["mon","tue","wen",[1,2,3,['a','b'],4],"thur","fri","sat","sun"]
print(days_of_week[3][3][1])
# slicing
print(days_of_week[0:3])
# ["start":"end":"action"]
print(days_of_week[0:3:2])
# modify
fruits = ["apple", "oranges", "mangoes", "bananas"]
fruits[0]="limes"
print(fruits)
# list methods
fruits = ["apple", "oranges", "mangoes", "bananas"]
# append
fruits.append("kiwi")
# copy
x=["wt","tk"]
x=fruits.copy()
# extend
x = ["wt", "tk"]
x.extend(fruits)
print(x)
print(x.index("oranges"))
# insert
fruits.insert(1,"kiwi")
print(fruits)
# pop
fruits.pop()
# remove
fruits.remove("bananas")
# 
fruits.sort()
print(fruits)
