# Databricks notebook source
answer = input("Do you like traveling: y/n? ")
if answer == "y":
    print("Good for you")
    answer2 = input("Have you been to India: y/n? ")
    if answer2 == "y":
       print("Nice")
    elif answer2 == "n":
        print("Your loss")
    else: 
        print("Invalid Answer")

elif answer == "n":
    print("Your loss")
else:
    print("Invalid Answer")


# COMMAND ----------




# COMMAND ----------


