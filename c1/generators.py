# Databricks notebook source
def get_number():
    for i in range(1,4):
        yield i

print(get_number())

# COMMAND ----------

generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))

# COMMAND ----------

for x in get_number():
    print(x)

# COMMAND ----------

numbers = list(get_number())
print(numbers)

# COMMAND ----------


