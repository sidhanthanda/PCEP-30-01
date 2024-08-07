# Databricks notebook source
thelist = ["Los Angeles", "Brampton", "London", "New York"]
counter = 0

for str in thelist:
    print(str)
    counter += 1
    print(counter)

# COMMAND ----------

print(thelist)
thelist[0]

#printing by index of the list. index 0 means the first element of the list

# COMMAND ----------

print(thelist)
thelist[-1]

#this starts to print the last element of the list

# COMMAND ----------

print(thelist)
thelist[-2]

#this prints the second last element of the list

# COMMAND ----------

print(thelist)
thelist[-4]

#this takes the fourth last item, which is the first 

# COMMAND ----------

print(thelist)
thelist[-5]

# #cannot take the fifth last item, will throw an error

# COMMAND ----------

print(thelist)
thelist[0:2]

#prints everything from the first index to the third index, excluding the third but including the first index

# COMMAND ----------

thelist[:]
#prints the list from first element to the last element. you could also do print(thelist)

# COMMAND ----------

thelist[30:360]
#there are no elements beyond 4, so it returns you back a blank list

# COMMAND ----------

listno2= ['Los Angeles', 'Brampton', 'London', 'New York', "Tokyo"]
del listno2[4]
listno2

# COMMAND ----------

listno2= ['Los Angeles', 'Brampton', 'London', 'New York', "Tokyo"]
del listno2[1:]
print(listno2)

# deletes all these elements from index 1 onwards, to the last element in the list

# COMMAND ----------

listno2= ['Los Angeles', 'Brampton', 'London', 'New York', "Tokyo"]
del listno2[:]
print(listno2)

# clears all elements from the list

# COMMAND ----------

# listno2= ['Los Angeles', 'Brampton', 'London', 'New York', "Tokyo"]
# del listno2
# print(listno2)

# # removes listno2 from existence

# COMMAND ----------

bookratings = [12, 8, 19, 24, 13]
bookratings.append(5)
print(bookratings)

# COMMAND ----------

bookratings = [12, 8, 19, 24, 13]
bookratings.insert(2, 10)
print(bookratings)

#this puts a new value, 10, at the third position of the list

# COMMAND ----------

a = 5
b = 1
c = a > b or b < a and a == 1
print(c)






# COMMAND ----------

thelist
for city in thelist:
    print("Current City: ", city)

# COMMAND ----------

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index])


# COMMAND ----------

spending = [20.49, 87.56, 19.45, 18.12, 36.40]
cost = 0.0

for number in spending:
    cost += number 

print("Total spent:", cost)


# COMMAND ----------


