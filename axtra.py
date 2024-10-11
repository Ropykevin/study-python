# Question1: Write a Python program that checks if a variable num is positive. If it is , further check if it is divisible by both 2 and 3. Print appropriate messages for each case.

num = int(input("enter a number: "))
if num > 0:
	check1 = "positive number"
	if num % 2 == 0 and num % 3 == 0:
		check = "conditions were met"
	else:
		check = "conditions not met"
else:
	check1 = "enter a valid number"

print(check1)
print(check)
# Question2: Write a Python program that checks a username and password. If both are correct, print "Login successful". If either the username or password is incorrect, print "Login failed".
username = input("enter you username: ")
password = input("enter you password: ")

correct_username = "Kevin"
correct_password = "12345"

if username == correct_username and password == correct_password:
	check = "login successful"
else:
	check ="login failed"
print(check)

# Question3: Write a Python program that checks if a given string is a palindrome(reads the same forward and backward)
word1 = input("enter word: ")
if word1 == word1[::-1]:
	print("palindrome word")
else:
	print("not a palindrome word")
f_name="Techcamp"
print(f_name[::-1])
# Question4: Write a Python program that calculates the Body Mass Index(BMI) and categorizes it into Underweight, Normal weight, Overweight, and Obesity based on standard BMI ranges.
weigth=float(input("enter weigth in kgs"))
heigth = float(input("enter heigth in meters"))

bmi=weigth/heigth**2
if bmi>=18.5 and bmi<=24.9:
	print("normal weight")
elif bmi>=25 and bmi<=29.9:
	print("over weigth")
elif bmi>=30:
	print("obesity")
else:
	print("under weigth")

# Question5: Write a Python program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# NB research on python loops
