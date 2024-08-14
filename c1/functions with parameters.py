# Databricks notebook source
input = [5.0, 6.5, 7.8, 12.9, 14.5, ]   

inputlen = len(input)

def averager(input):
    sum = 0.0
    for number in input:
        sum += number
    average = sum/inputlen
    print(average)

averager(input)



# COMMAND ----------

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count("Joker", "k")

# COMMAND ----------

print_letter_count(text="Welcome", letter="e")

# COMMAND ----------


