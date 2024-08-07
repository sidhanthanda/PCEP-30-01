# Databricks notebook source
counter =1 
while counter < 25:
    print(counter)
    print("Increasing")
    counter +=1
print("Finished")

# COMMAND ----------

secret_number = 14
user_input = int(input("Try to guess the secret number from 0 to 20: "))
while user_input != secret_number:
    print("Wrong!")
    user_input = int(input("Try to guess the secret number from 0 to 20: "))
print("Perfect! You have guessed the secret number.")


# COMMAND ----------

word = "hello!"
for letter in word:
    print(letter)
#! point counts as a letter

# COMMAND ----------

for counter in range (1,11):
    print(counter)
print("Finished!")

# COMMAND ----------

for counter in range (1,11, 5):
    print(counter)
print("Finished!")
#third number is the "step" value. now it prints all values from 1 to 10 in increments of 5, starting at 1. so 1, 6, thats it.

# COMMAND ----------

while True:
    name = input("Enter your name or EXIT to close the program: ")
    if (name == "EXIT"):
        # If 'EXIT' is entered, break out of the loop, effectively ending the program
        break
    print("Hello", name)

# COMMAND ----------

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)


# COMMAND ----------

for i in range (11):
    pass

# COMMAND ----------

for a in range (1 ,6):
    for b in range(1, 6):
        print(a, 'x', b, '=', a*b)

# COMMAND ----------

a = 5
b = 1
c = a > b or b < a and a == 1
print(c)

# COMMAND ----------



# COMMAND ----------

i = 1
while i < 5:
    print(i, end=' ')
    i += 1
else:
    print(i, end=' ')

# COMMAND ----------


