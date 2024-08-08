# Databricks notebook source
cells = [["Hello", "Greetings", "Bonjour"], ["Bye", "Goodbye", "Au revoir"]]
cells[0]

# COMMAND ----------

cells[0][0]

# COMMAND ----------

cells[1][2]

# COMMAND ----------

for x in cells:
    print("Element:", x)

# COMMAND ----------

for x in cells:
    for y in x:
        print("Element:", y)
        

# COMMAND ----------

table = [["Hello", "Greetings", "Bonjour"], ["Bye", "Goodbye", "Au revoir"]]

#makes more sense
for row in table:
    for cell in row:
        print("Element:", cell)

# COMMAND ----------

table = [["1", "2", "3"], ["A", "B", "C"]]

#makes more sense
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()

# COMMAND ----------

table = [[i for i in range(1, 6)] for j in range (4)]
print(table)

# COMMAND ----------


