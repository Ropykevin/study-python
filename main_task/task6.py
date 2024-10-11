# TASK 6: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message, the account is blocked.
# Once you learn functions, revisit this and write this code inside a function.]
correct_password = "admin@123"
attempts=4 
for i in range(attempts):
    password = input("Enter your password: ")
    if password==correct_password :
        print("Access granted")
        break
    else:
        rem_att=attempts-(i+1)
        print(f"Wrong password. {rem_att} attempts left try again!")
        if rem_att==0:
            print("account blocked")
        else:
            continue