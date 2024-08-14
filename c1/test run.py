# Databricks notebook source
def print_letter_count(text="Hello", letter="a"):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

# COMMAND ----------

print_letter_count(text="Hello")

# COMMAND ----------


