# Databricks notebook source
#a function is a block of code that performs a specific activity when it is called
# helps to store code that is most commonly used
#most of the time, functions will return values
#python has some inbuilt functions like print(), input(), etc
#you can also make user defined functions.
#a function has to be defined properly  before it is used
#def function_name():
#function_body

# COMMAND ----------

#this function is properly defined, but not called
def func():
    print("Inside this function")


# COMMAND ----------

#this function is defined and called

def function(): #it is defined here
    print("This function will be called")

function()  #it is called here

# COMMAND ----------

function()
print("bye")

# COMMAND ----------

second_func() #function is called

def second_func(): #function is defined
    print("Hello!")

#run this code

# COMMAND ----------

#that should have thrown an error
#this is because you have to define the function before you call it

def second_fun():
    print("Hello!")

second_fun()


# COMMAND ----------

def hello(age):  # Function defined to take one parameter 'age'
    print("Your age is", age)  # This line prints the age to the console

age = input("Enter your age:")  # User input is taken and stored in variable 'age' as a string

hello(age)  # The 'hello' function is called with 'age' as the argument

# The function 'hello()' is defined to print a message that includes the age given to it.
# The 'age' variable is set by the user input through the 'input()' function, which returns a string.
# After the 'age' is defined, the function 'hello()' is called with 'age' as the argument, correctly using the value entered by the user.


# COMMAND ----------

# Parameters

def currentage(year_born):  # 'year_born' here is a parameter. It acts as a placeholder that will take any value passed to this function when it is called.
    subtractor = 2024 - year_born  # 'subtractor' calculates the age by subtracting the year_born from the current year (2024).
    print("Your age is:", subtractor)  # Prints the calculated age.

year_born = int(input("What year were you born in?"))  # User is prompted to input their birth year. This input is converted to an integer and stored in 'year_born'.

currentage(year_born)  # The value stored in 'year_born' is passed to the 'currentage' function. Here, 'year_born' acts as an argument.
# This argument (the user's input) replaces the parameter 'year_born' within the function for the duration of the function call.


# COMMAND ----------

# Arguments 

def display_favorite_color(color):  # 'color' here is a parameter, a placeholder ready to accept any value passed when the function is called.
    print("Your favorite color is:", color)  # This prints the favorite color.

favorite_color = input("What is your favorite color? ")  # User is prompted to input their favorite color, and the response is stored in 'favorite_color'.

display_favorite_color(favorite_color)  # The value stored in 'favorite_color' is passed to the 'display_favorite_color' function. Here, 'favorite_color' is an argument.
# The argument 'favorite_color' fills in for the parameter 'color' within the function. This actual value is what the function uses during its execution.
# This shows how arguments are the actual data supplied to the function, directly influencing the output of the function based on user input.


# COMMAND ----------

#Using lists as arguments
def sq_sum(ls):
    sum = 0
    for number in ls:
        sq = number ** 2
        sum = sq + sum
    print(sum)

l1 = [10, 2, 4, 5, 4, 2]
l2 = [1, 4, 6, 7, 8, 9]

sq_sum(l1)  # Call using l1
sq_sum(l2)  # Call using l2


# COMMAND ----------

#Using lists as arguments
def sq_sum(ls):
    sum = 0
    for number in ls:
        sq = number ** 2
        sum = sq + sum
    print(sum)
    print(l1)
    print(l2)
    print(x)

x = 10
l1 = [10, 2, 4, 5, 4, 2]
l2 = [1, 4, 6, 7, 8, 9]

sq_sum(l1)  # Call using l1
sq_sum(l2)  # Call using l2


# COMMAND ----------

def listalter(ls):
    del ls[2]  # Delete the element at index 2 of the passed list
    print("Inside list value:", ls)

thelist = ["Hello", "There", "General", "Kenobi"]
print("1. List:", thelist)
listalter(thelist)
print("2. List:", thelist)


# COMMAND ----------

def hello(age):
    print("Your age is "+ age)

hello("35")

# COMMAND ----------

def hello(age,pnumber, name):
    print("Age:", age)
    print("Phone Number:", pnumber )
    print("Name:", name)


age = int(input("Enter your age: "))
pnumber = int(input("Enter your phone number with spaces between each digit: "))
name = input("Enter your name: ")

hello(age, pnumber, name)

# COMMAND ----------


