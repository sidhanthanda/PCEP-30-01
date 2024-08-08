# Databricks notebook source
band = "Iron Maiden"
print(band[7])

# COMMAND ----------

print(band[:8])

# COMMAND ----------

lowercase= "uncapitalized swine"
fixed = lowercase.upper()
print(fixed)

# COMMAND ----------

UPPERCASE = "I AM YELLING"
rectified = UPPERCASE.lower()
print(rectified)

# COMMAND ----------

user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')


# COMMAND ----------


