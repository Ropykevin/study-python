# 5. Reverse 987 to 789 without using an inbuilt - method or Assigning 789 manually.
# Hint: Strings can be reversed using[::]
# 
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76, "John")]
# get 987 from my_ds
print(my_ds[4])
# convert into a String
my_ds[4]=str(my_ds[4])
print(type(my_ds[4]))
# reverse using  [::]
my_ds[4]=my_ds[4][2::-1]
my_ds[4]=int(my_ds[4])
print(my_ds)
# convert back to an interger


# dict={
#     1:"ginger"
# }
# print(dict[1])