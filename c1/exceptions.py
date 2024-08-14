# Databricks notebook source
value = int(input("Enter an integer: "))
print("The inverse of", value, "is", 1/value)

# COMMAND ----------

try:
    value = int(input("Enter an integer: "))
    print("The inverse of", value, "is", 1/value)
except:
    print("You did not provide a number")

# COMMAND ----------

try:
    value = int(input("Enter an integer: "))
    print("The inverse of", value, "is", 1/value)
except ValueError:
    print("You did not provide a number")
except ZeroDivisionError:
    print("You gave 0 and division by 0 cannot be done")

# COMMAND ----------

try:
    value = int(input("Enter an integer: "))
    print("The inverse of", value, "is", 1/value)
except ValueError:
    print("You did not provide a number")
except ZeroDivisionError:
    print("You gave 0 and division by 0 cannot be done")
except:
    print("Something unexpectedly unexpected happened!")

# COMMAND ----------


