# Databricks notebook source
print("Welcome to this thing")
account_exist = input("Do you have an account? N/Y? ")
username_details = []
password_details = []

if account_exist == "N":
    print("Make an account here. ")
    new_username = input("Enter your username: ")
    new_password = input("Enter your new password: ")
    username_details.append(new_username)
    password_details.append(new_password)
    print("Thank you for creating your new account.")
    print("Please log in.")
elif account_exist == "Y":
    print("Welcome back.")
    username = input("Enter your username here: ")
    password = input("Enter password here: ")
    if username in username_details and password in password_details:
        user_index = username_details.index(username)
        if password_details[user_index] == password:
            print("Login successful!")
        else:
            print("Wrong password!")
    else:
        print("Username not found!")

else: 
    print("Invalid response")

