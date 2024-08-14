# Databricks notebook source
emails = {
    "David Hasselhoff": "dh@gmail.com",
    "Bob J. Nerik": "gmail@email.com",
    "Susan Peter": "sp@name.com"
}

print(emails["Bob J. Nerik"])

# COMMAND ----------

french_animals = {
    #key : #value
    "dog": "chien",
    "female dog": "chienne",
    "cat": "chat",
    "female cat": "chatte"
}

print(french_animals["dog"])

# COMMAND ----------

print(type(french_animals))

# COMMAND ----------

print(french_animals["chat"])
#shows an error, because dictionaries are one-way only

# COMMAND ----------

tennis_ranking = {
    [1]: 'Ashleigh Barty',
    [2]: 'Naomi Osaka',
    [3]: 'Simona Halep'
}

#invalid syntax, no square brackets around the keys

# COMMAND ----------

grades = {}

grades['John'] = 'A-'
grades['Anne'] = 'B'

print(grades)

grades['Anne'] = 'A'

print(grades)

grades.update({'John': 'A'})

print(grades)  


# COMMAND ----------

if "John" in grades:
    print("John got: ", grades["John"])
    

# COMMAND ----------

del grades["John"]
print(grades)

# COMMAND ----------

grades = {}
grades ["John"] = "A-"
grades["Anne"]= "B"

for el in grades:
    print(el)

for el in grades.keys():
    print(el)

# COMMAND ----------

for el in grades.values():
    print(el)

# COMMAND ----------

for person, grades in grades.items():
    print(person, "got", grades)

# COMMAND ----------



nicks = {'Adam': 'Smasher', 'Kate': 'k4t3', 'John': 'xJohnx'}
 
if 'k4t3' in nicks.keys():
  print('a')
 
if 'k4t3' in nicks.values():
  print('b')





# COMMAND ----------

    
