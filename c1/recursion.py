# Databricks notebook source
def factorial(number):
    factorial = 1
    for x in range (1, number +1):
        factorial *= x
    return factorial

print(factorial(6))

# COMMAND ----------

def get_factorial_recursive(number):
    return number * get_factorial_recursive(number-1)

# COMMAND ----------

get_factorial_recursive(6)

# COMMAND ----------

def get_factorial_recursive(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursive(number-1)

# COMMAND ----------

get_factorial_recursive(6)

# COMMAND ----------


