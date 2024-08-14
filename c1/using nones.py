# Databricks notebook source
print("Hello")

# COMMAND ----------

length = len("Hello")

# COMMAND ----------

print_return = print("Hello World!")
print(print_return)


# COMMAND ----------

x = None
if x:
    print("None is true")
elif x is False:
    print("None is false")
else:
    print("None is not True, or False, None is None")

# COMMAND ----------

x = None
if x is None:
    print("Yes")
if x == None:
    print("It does!")

# COMMAND ----------

def greet():
    print("Hello!")

x = greet()
print(x)

# COMMAND ----------


