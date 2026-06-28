'''
Variable name must start with a letter or an underscore (_), followed by letters, numbers, or underscores.
variable names cannot start with a number and cannot contain spaces or special characters (except for underscores).
variable names are case-sensitive (e.g., myVar and myvar are different variables).
Examples of valid variable names: my_variable, age, _temp, userName
Examples of invalid variable names: 2ndVariable, my variable, user-name
'''

'''
Multiple variable assignment :-
Camel case: myVariableName
Snake case: my_variable_name
Pascal case: MyVariableName
'''

#Variable = value and printing it
age = 25
height = 6.1
print("Age is :", age)
print("Height is :", height)

# Formatted output (f-strings)
# Put an 'f' before the opening quote and wrap variables in {curly braces}
animal = "fox"
action = "jumped"
print(f"The quick brown {animal} {action} over the lazy dog.")

# Type conversion with input
# We wrap the input() function inside int() or float() to convert the data type immediately
favorite_number = int(input("Enter your favorite whole number: "))
temperature = float(input("Enter the current temperature in Fahrenheit (e.g., 98.6): "))
print(f"Your number multiplied by 2 is {favorite_number * 2}")
print(f"The temperature in Celsius is {(temperature - 32) * 5/9:.2f}°C")

#Greeting User 
name = input("What is your name? ")
print(f"It is great to meet you, {name}! Have a wonderful day.")

#Same values for multiple variables
x = y = z = 10
print(f"x = {x}, y = {y}, z = {z}")

#Adding variables (concatenation)
print("Hi" + " " + "Good Morning") #Space between words
print("Rap" + "er") #No space between words

#Assigning multiple values to multiple variables
a , b = 5 , 10
print("Value of a is :", a)
print("Value of b is :", b) 

# Keywords are reserved words in Python that have special meanings and cannot be used as variable names.
# Ex : if, else, for, while, def, class, import, from, as, with, try, except, finally, raise, 
#    : assert, del, lambda, nonlocal, global, yield, return, pass, break, continue etc...
# Returns error if = 10 print(if) (if is a keyword and cannot be used as a variable name)