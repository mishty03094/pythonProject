'''Write a program in python that checks if a string starts with a given prefix
or ends with a given suffix'''
str1=input("enter string")
prefix=input("enter prefix")
range1=len(prefix)
print((str1[:range1]==prefix))
suffix=input("enter suffix")
range2=len(str1)-len(suffix)
print(str1[range2:]==suffix)