''' Write a python program that removes all punctuation from a given string'''
str1=input("enter string: ")
punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
cleaned_string = ""

for char in str1:
    if char not in punctuation:
        cleaned_string += char

print("String without punctuation:", cleaned_string)
