# Questions
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
temp=round(temp)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89
temp = 56.8926
temp = round(temp, 2)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893
temp = 56.8926
temp = round(temp, 3)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 8.926
# NB: Use string  slice & concatenation, but have result as float
temp = 56.8926
# convert to str
temp=str(temp)
# slice
temp=temp[3:7]#8926
temp=temp[0]+"."+temp[1:]
temp=float(temp)
print(temp)
# temp=float(temp)
# x=temp
# y=1000
# temp=x/y
# print(temp)

# Attempt questions below. Whether you get the right answer or not , still read the solution explanation.
# https: // realpython.com/quizzes/python-data-types/
