# Databricks notebook source
tuple = ()
onevaltuple1 = (1, )
onevaltuple2 = 1,
threeevaltuple = 1,2,3

print(threeevaltuple)

# COMMAND ----------

user_data = ('John', 'American', 1964)
print(len(user_data))


# COMMAND ----------

user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US!')


# COMMAND ----------

user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)


# COMMAND ----------

user_data = ("John", "American", 1964) + ("teacher", "male")
print(user_data)

# COMMAND ----------

number = (0, 1) * 256
print(number)

# COMMAND ----------

city_1 = ('London', 'UK', 9.98)

city_2 = ('Canberra', 'Australia', 0.4)

city_3 = ('Algiers', 'Algeria', 3.9)

capitals = city_1 + city_2 + city_3
capitals

# COMMAND ----------



# COMMAND ----------


