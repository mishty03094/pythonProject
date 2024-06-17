'''Write a program that takes a string input from the user and writes it to a
text file.'''
user_input = input("Please enter a string to write to the file: ")


file_name = "output.txt"


file= open(file_name, "w")
file.write(user_input)