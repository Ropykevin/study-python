def hello():
    name="kevin"
    print(f"Hello, {name}!")
    
hello()

#  create a function that calculates the area of a triangle
def triangle_area():
    base=20
    height=10
    area=(base*height)*0.5
    print(area)
triangle_area()

#  create a function that calculates the area of a rectangle take the users input

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area} square units")
rectangle_area()

# create a function that checks if a number is an even number take the users input of the number

def check_number():
    num=int(input("enter a number: "))
    if num%2==0:
        print("even number")
    else:
        print("odd number")
        
check_number()

# 3,8,10,12,13 using functions

# parameters=>a variable only used inside a fuction
# arguments=>is the exact value passed when calling a function

