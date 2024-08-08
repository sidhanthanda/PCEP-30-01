# Databricks notebook source
numbers = [1, 2, 3, 4]


# COMMAND ----------

numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# COMMAND ----------

# Create a list called 'numbers' that holds the numbers
numbers = [i for i in range(1, 26)]  # This is called a list comprehension

# 'for i in range(1, 26)' means we want to look at each number starting from 1 up to 25
# 'i' is the number we are looking at each time, and we want to add that number to our list
# this makes a list with all the numbers from 1 to 25

print(numbers) 

# COMMAND ----------

numbers = [i for i in range(1, 26) if i % 3 != 0]  

# We are making a list of numbers from 1 to 25, but skipping any number that is divisible by 3

print(numbers)

# COMMAND ----------


