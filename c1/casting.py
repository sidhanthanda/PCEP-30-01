# Databricks notebook source
height = input("Height Converter: enter your height in cm: ")
float_heightcm= float(height)
print("Your height in feet is:", float_heightcm/30.48)

# COMMAND ----------

yearborn = int(input("Wht year were you born?"))
print("In 2100, you will be", 2100-yearborn, "years old")

# COMMAND ----------

tempc = input("Enter the temperature today in celsius: ")
tempf = float(tempc) * 1.8 +32
tempfinal = str(tempc) + " degress celsius equals " + str(tempf) + " degrees farenheit"
print(tempfinal)

# COMMAND ----------


