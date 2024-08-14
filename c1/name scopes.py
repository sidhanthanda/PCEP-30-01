# Databricks notebook source
def reveal_ancient_lore():
    thelore = "Surprise!"
    print(thelore)

thelore = "Hello"
print(thelore)
reveal_ancient_lore()
print(thelore)

# COMMAND ----------

def reveal_ancient_lore():
    global thelore
    thelore = "Surprise!"
    print(thelore)

thelore = "Hello"
print(thelore)
reveal_ancient_lore()
print(thelore)


# COMMAND ----------

def reveal_ancient_lore():
    thelore.append("Surprise!")
    print(thelore)

thelore = ["Hello"]
print(thelore)
reveal_ancient_lore()
print(thelore)


# COMMAND ----------


