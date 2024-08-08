# Databricks notebook source
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)


# COMMAND ----------

list1 = [1, 2, 3]
list2 = list1
list1[0] = -5
print("Original: ", list1, "\nNew:", list2)

# COMMAND ----------

list1 = [1, 2, 3]
list2 = list1[:]
list1[0] = -5
print("Original: ", list1, "\nNew:", list2)

# COMMAND ----------


