 # A variable is like a labeled box where you can store data. Imagine you have a box labeled "age" and you put the number 25 in it. In Python, you would do this by writing age = 25. This means you're storing the number 25 in the variable named age.

#ere's the cool part: whenever you use age in your code, Python will remember it is 25. For example, if you write print(age), Python will show 25.

#Task
#Create a variable in editor named age and assign the value 25 to it.
#Print the value of age variable using print statement.
#Notice how we don't use " " (double quotes) when printing variables.


# Replace __ with 25

age = 25
print(age)

#There are many different types of variables in Python. The type of a variable is defined by the kind of value it stores.

#Some variable types in Python are as follows

# Numeric variables - hold integers and decimal values
#age = 25
#temperature = 98.6

# String variables - Stores a sequence of characters enclosed in single or double quotes
#name = "John Doe"
#message = 'Hello, world!'

# Boolean variables - only hold the values true and false
#is_true = True
#is_false = False

# List variables - Stores a collection of items, which can be of different types.
#numbers = [1, 2, 3, 4, 5]
#fruits = ['apple', 'banana', 'orange']

# Tuple variables
#coordinates = (10, 20)

# Dictionary variables
#person = {'name': 'Alice', 'age': 30}

# Set variables
#unique_numbers = {1, 2, 3}

# None variable
#empty_value = None
#We will learn about all of them in coming lessons.

#Task
#Write a program which does the following

#There is a variable named number having value 20 in the editor.
#Use the print command to output the value of (number - 1)

number = 20
print(number -1)

#We learned that variable is a labelled box which can store many different types of values. You can also change the value of a variable in your code.

#For example

#age = 25
#print(age)

# Update age
#age = 26
#print(age)
#The above code will output

#25
#26
#We are going to use variables all the time in the coming lessons. So let's learn a few more stuff about them.

#Rules for Python variable names:

#A variable name can only contain alphabets, numbers and underscores (ie. A-Z, a-z, 0-9, and _).
#A variable name cannot start with a number.
#A variable name cannot have spaces in between.
#Variable names are case-sensitive (age, Age and AGE are three different variables).
#Be sure to follow these rules when creating a variable to not get errors.

#Task
#There is some code written in the editor to print "Code Chef". But the variable names are not following the rule. Can you spot the mistake and fix it?
first_name = "code"
last_name = "chef"
print(first_name, last_name)

#Write a program which does the following

#Declare two variables

a=23
b=20

print (a+b)

#Write a program which does the following

#Find out and display the area of a rectangle of sides 45 and 76 respectively.
#Declare variables length, width and area and assign the relevant values to them
#Output the value of variable area 



length = 45
width = 76
area = length * width

print(area)


#Write a program which does the following:

#Find the area of a circle whose radius is 8.9. Take pi = 3.14
#Declare variables radius , pi and area and assign the relevant values to them
#Output the area, you don't need to output any other text.
#Note: Formula for the area of a circle is pi×radius×radius

pi = 3.14
radius = 8.9

area = pi*radius*radius

print(area)


#The string type is used to store a sequence of characters, i.e. text.
#String values can be surrounded by either double quotes or single quotes. Python does not care about whether you use single or double quotes.

#For example, both the below codes do the same thing: Declare a variable with value I am using CodeChef.
# sentence1 = "I am using CodeChef"
# sentence2 = 'I am using CodeChef'

#Task
#Write a program which does the following

#Declare two variables a and b
#Assign Learning to a and is fun! to b
#Using the concepts we learned previously, display the sentence "Learning is fun!" using variables a and b in a single line

a="Learning"
b="is fun!"

print(a,b)

#Hope you got the real taste of writing code in the last few problems.

#Till now we have learned about printing single and multiple values. We also learned about variables, rules for naming variables and different data types.

#Next up is a small quiz on what we have learned till now.

#Then we are going to learn about another data type in the next lesson and solve slightly harder problems to deeply understand how Python works.

#This knowledge will make you a master in Python real soon. Don't get discouraged when you get Wrong answer or Runtime error. Everybody makes mistakes while learning something.