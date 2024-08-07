# Databricks notebook source
age = int(input("What is your age: "))  
country = input("What is your country: ")  

if age < 25 and country == "Germany":  
    print("You are under 25 and from Germany.")  
else:
    print("You are not from Germany")

# COMMAND ----------

country = input("What is your country: ")

if country == "Sweden" or country == "Britain" or country == "Norway":  
    print("You are from Europe")
else:
    print("You are not from Europe")

# COMMAND ----------


