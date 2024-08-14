# Databricks notebook source
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average

print("The average is:", get_average([5.0, 6.5, 7.8, 12.9, 14.5]))


# COMMAND ----------

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print("Behold!")


get_average([2])

# COMMAND ----------

def is_first_last_equal(number_list):
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False


# COMMAND ----------

print(is_first_last_equal([20, 80, 2651, 20]))

# COMMAND ----------


