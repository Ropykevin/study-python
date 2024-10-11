# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

# calculating total_marks

def calc_total_marks(a,b,c,d,e):
    total_marks=a+b+c+d+e
    return total_marks

maths=int(input("enter maths: "))
eng=int(input("enter eng marks"))
swa=int(input('enter swa:'))
sci = int(input('enter sci:'))
sos = int(input('enter sos:'))

total=calc_total_marks(maths,eng,swa,sci,sos)
print(total)

# calculating average 
def calc_average(av):
    average=av/5
    return average

avg=calc_average(total)
print(avg)
# finding the grades
def find_grade(average):
    if average >=0 and average<=100:
        if average > 79:
            grade="A"
        elif average >= 60 and average <= 79:
            grade="B"
        elif average >49 and average <= 59:
            grade="C"
        elif average>40 and average<=49:
            grade="D"
        else:
            grade="E"
    else:
        grade="Invalid average"
    return grade

# printing the grade
grade=find_grade(avg)
print(grade)
