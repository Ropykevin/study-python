# # def hello():
# #     name = "kevin"
# #     print(f"Hello, {name}!")
# # hello()

# def hello(name):
#     print(f"Hello, {name}!")

# hello("kimani")
# hello("arnold")
# hello("andrew")

# #  create a function that calculates the area of a triangle parameters and arguments 2
# def triangle_are(a,b):
#     area=(a*b)*0.5
#     return (f"the area is{area}")
# y=triangle_are(20,10)
# z=triangle_are(50,30)
# #  create a function that calculates the area of a rectangle take the users input  use parameters and arguments 
# def rectangle_area(length,width):
#     area=length*width
#     return area

# len=int(input("enter the length: "))
# width=int(input("enter width: "))

# x=rectangle_area(len,width)
# print(x)

# # create a function that checks if a number is an even number take the users input of the number

# def even_number(num):
#     if num %2 ==0 :
#         value="even number"
#     else:
#         value="odd number"
#     return value

# number=int(input("enter number: "))
# e_num = even_number(number)
# print(e_num)

# # 3,8,10,12,13 using functions


# # create a function that checks if a number is an even number


# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Once you learn functions, revisit this and write this code inside a function. 

def largest_number(a,b,c,d):
    if a>b and a>c and a>d:
        value=f"{a} is the largest"
    elif b>a and b>c and b>d:
        value=f"{b} is the largest"
    elif c>a and c>b and c>d:
        value=f"{c} is the largest"
    else:
        value=f"{d} is the largest"
    return value
    
num1=int(input("enter number 1: "))
num2=int(input("enter number 2 : "))
num3=int(input("enter number 3: "))
num4=int(input("enter number 4: "))

largest_num=largest_number(num1,num2,num3,num4)
print(largest_num)