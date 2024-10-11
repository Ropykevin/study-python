x=10
if x>20:
    print("x is greater")
else:
    print("x is less than")

# take a users input on a number
# check if the number is even
# else display odd number

number=input("enter a number: ")
number=int(number)
if number%2==0:
    print("number is even")
else:
    print("number is odd")

# take a users input on a number
# check if the number is odd and greater 50
# else display even number

number1=int(input("enter number: "))

if (number1%2!=0) and (number1>50) :
    print("number is odd and greater than 50")
else:
    print("number is even or less than 50 ")

# if 10 > 5:
# 	print("10 is greater")
# else:
# 	print("10 is less than")

x = int(input("enter x: "))
y = int(input("enter y: "))
if 20>=x>10 and y>100:
    print("conditions met")
else:
    print("conditions not met")

# take users input of marks
# find the grade using the following conditions
# marks above 80 A
# marks above 70 B
# marks above 60 C
# marks above 50 D
# otherwise E
# if elif else

marks1=int(input("enter marks: "))

if marks1>=80:
    print("grade A")
elif marks1>=70 and marks1<80:
    print("grade B")
elif marks1>=60 and marks1 <70:
    print("grade c")
else:
    print("grade D")

# Nested if
# an if statement inside another if statement
# take users input of marks
# check if the marks is btw 0 and 100
# display invalid marks
# find the grade using the following conditions
# marks above 80 A
# marks above 70 B
# marks above 60 C
# marks above 50 D
# otherwise E
# if elif else

marks1 = int(input("enter marks: "))
if marks1 >=0 and marks1<=100:
    if marks1 >= 80:
        print("grade A")
    elif marks1 >= 70 and marks1 < 80:
        print("grade B")
    elif marks1 >= 60 and marks1 < 70:
        print("grade c")
    else:
        print("grade D")
else:
    print("invalid marks")
# Write a Python program that checks if a number num is positive, negative, or zero. If the number is positive, it should further check if it is even or odd.
