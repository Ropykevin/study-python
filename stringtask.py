# Create a new python file stringtask.py and attempt the 5 questions below:
# Clean up the following variable to give the clean version in lower case. 
# Using inbuilt methods in the str class
# my_name = “  JOHn  .“ to “john”
my_name = "  JOHn  ."
# to lower
my_name=my_name.lower()
# replace
my_name=my_name.replace(".","")

# strip
my_name=my_name.strip()
print(my_name)
# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” 
# only display “Clinton forces”
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])
# Split the below sentence using a semicolon i.e
# And display length of the result.
# “The lazy dog; ran so fast; it hit the wall.”
statement = "The lazy dog; ran so fast; it hit the wall."
statement=statement.split(";")
print(statement)
print(len(statement))
# first_name = "  Joh.n"  last_name = "   Do,e" Clean up and display Full name i.e John Doe
first_name = "  Joh.n"
last_name = "   Do,e"
first_name = first_name.strip().replace(".", "")
last_name=last_name.strip().replace(",","")
full_name=first_name+" "+ last_name
print(full_name)
# Having the string r = '["E","W","C"]'  # Manipulate it to display EWC
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
r = '["E","W","C"]'
r=r.replace("[","").replace('"',"").replace(",","").replace("]","")
print(r)