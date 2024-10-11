# Take three inputs from a user, separately. Print the largest of the numbers.

# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# num3 = int(input("enter third number:"))

# if num1>num2 and num1>num3:
#     print(f"{num1} is the largest")
# elif num2>num1 and num2>num3:
#     print(f"{num2} is the largest")
# else:
#     print(f"{num3} is the largest")

# # Hint: Determine what type of data is taken in as input.
# # Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

# temp=int(input("enter temperature"))

# if temp>30 :
#     value=("temperature is too high")
# elif temp >15:
#     value=("normal temperature")
# else:
#     value=("cold temperature")

# if temp>15 and temp<=30:
#     value = ("normal temperature")
# elif temp<15:
#     value = ("cold temperature")
# else:
#     value = ("temperature is too high")

# print(value)

# 3.Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

# x=int(input("enter x: "))
# y = int(input("enter y: "))
# if x>=10 and x<=20 and y>100:
#     res="conditions met"
# else:
#     res="conditions not met"
# print(res)

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is , print "Access   granted", otherwise print "Access denied"

password = input("enter password: ")
correct_password = "secret123"
if password == correct_password:
    check = "access granted"
else:
    check = "access Denied"

print(check)

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

student_score = int(input("enter score: "))
attendance = int(input("enter attendance: "))

if student_score > 90:
    if attendance > 80:
        val = "Excellent student"
    else:
        val = "Good score, but attendance needs improvement"
else:
    val = "poor"

print(val)
# Attempt the questions in the link below
# https: // realpython.com/quizzes/python-conditional-statements/
