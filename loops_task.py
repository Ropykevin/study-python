# Write a program that displays  numbers 1 to 50 inside a list.
x = list(range(1, 51))
print(x)  # Output: [1, 2, 3, 4,
# From 1 above display the ones divisible by 7 or 5 inside a list.
for i in x:
    if i % 7 == 0 or i % 5 == 0:
        print(i)
# Find sum and average of values in the range between 10 to 40.
sum = 0
y = list(range(11, 40))
for i in y:
    sum += i
print(sum)
average = sum/len(y)
print(average)
# Put in a list the first 10 odd numbers between 10 to 50.

a = list(range(10, 51))
odd_numbers = []
for b in a:
    if b % 2 != 0:
        odd_numbers.append(b)
        if len(odd_numbers) == 10:
            break
print(odd_numbers)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=int(input("enter number: "))
for i in range(1,11):
    mult=i * number
    print(f"{number} x {i} = {mult}")

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop 
even_count = 0
for i in range(1,50):
    if i % 2 == 0:
        # even_count=even_count+1
        even_count += 1
print(even_count)

# even_numbers=[]
# for i in range(1,50):
#     if i%2==0:
#         even_numbers.append(i)

# print(even_numbers)
# print(len(even_numbers))
total_quantity=0

ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]
for i in ls1:
    quantity=i[1]
    # total_quantity=total_quantity+quantity
    total_quantity += quantity
   
print(total_quantity)
# Display the total quantity of the 3 above.
