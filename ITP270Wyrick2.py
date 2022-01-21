#!/usr/bin/python3

print("Welcome to the ITP270 Spring 2022 course!")

user_choice =input("Do you want to proceed with the program?[Y/N]")

if user_choice == "Y":
	user_name = input("")
	user_course = input("")
	print("Thanks " + user_name + " for taking the course " + user_course + ".")
else:
	print("Have a good day!")
