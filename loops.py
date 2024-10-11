x = [1, 2, 3, 4, 5,6]
for i in x:
    print(x)
	
# display a list of numbers btw 0 ,1000
range(10,1000)
y = list(range(10,1000))

for i in y:
    print(i)

# iterate through numbers btw 20 and 100 only display even numbers
even_numbers=[]
for i in range(20,100):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

# break it stops the loop

for i in range(51):
    print(i)
    if i ==3:
        break
    

