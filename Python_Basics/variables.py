# variables this is the way to store the data in computer's memore
# store name / String charaters
person_name = "David"
print(person_name)
# store numbers like age or float like height
person_age = 25
person_height = 6.2
print(person_age, person_height)

# we can store the data in different types or forms:
# which is categorized in :
# 1. Primitive and Non-Primitive type

# Python is an case sensitive language like the boolean works only when True or False
# rather than using true/TRUE or FALSE/false is used

education_status = True
married_status = False  # don't use false/FALSE
university_name = "Harvard University"

# email format in string variable
email_message = """
hi,
this is David writting this mail to 
thank you for the feedback
"""
# In built funtion to get String length
# A function is a peace code which execute/performs or carries out a task and it is completely reusable.

# get length of the String

print(len(university_name))  # output: 18

# to access the charecters of string
print(university_name[0])  # output: H
print(university_name[2])  # output: r
print(university_name[-1])  # output: y
print(university_name[0:4])  # output: Harv
print(university_name[0:])  # output: Harvard University
print(university_name[:4])  # output: Harv
print(university_name[:])  # output: Harvard University
