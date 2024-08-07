# Databricks notebook source
#logical operators

#< less than
#> greater  than
#<= less than equal to
#>= greater than equal to
#== equal to
#!= not equal to

# COMMAND ----------

password = input("Enter the password: ")
if password == "Xx__password__xX":
    print("Correct")
else:
    print("Try Again!")

# COMMAND ----------

if 1 == 2:
    print("True")

# COMMAND ----------

if 2 == 2:
    print("True")

# COMMAND ----------

if 2.0 == 2:
    print("True")
#python converts the 2 to float, so they are equal
