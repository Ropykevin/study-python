# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions, revisit this and write this code inside a function.
# while true always loop until it finds break

while True:
    num1=input("enter number1: ")
    num2=input("enter number2: ")
    if (num1.isdigit() and num2.isdigit()) :
        num1=int(num1)
        num2=int(num2)
        sum=num1+num2
        break
    else:
        print("invalid character entered")
            
            

print(sum)