# Databricks notebook source
first = input("Enter first number: ")
second = input("Enter second number: ")
print("Before swapping:", first, second)
first = second
second = first
print("After swapping: ", first, second)
#first is 15
#second is 24
#this doesn't work

# COMMAND ----------

first = input("Enter first number: ")
second = input("Enter second number: ")
print("Before swapping:", first, second)
temp = first
first = second
second = temp
print("After swapping: ", first, second)
#same numbers as before
#this works

# COMMAND ----------

first = input("Enter first number: ")
second = input("Enter second number: ")
print("Before swapping:", first, second)
first, second = second, first
print("After swapping: ", first, second)


# COMMAND ----------

devices = ["Book", "Tablet", "Computer", "PC", "Phone"]
print(devices)
devices[0], devices[4] = devices[4], devices[0]
print(devices)

# COMMAND ----------

random_nos = [8, 90, 30, 360, 2400, 50, 300]
random_nos.sort()
print(random_nos)

# COMMAND ----------

random_nos = [8, 90, 30, 360, 2400, 50, 300]
random_nos.sort(reverse=True)
print(random_nos)

# COMMAND ----------

print(sorted(random_nos))
print(random_nos)

# COMMAND ----------


