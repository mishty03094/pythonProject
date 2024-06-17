'''Write a python program that returns the minimum and maximum values
in a list of numbers.'''
l1=[]
n=int(input("enter length: "))
sum=0
for i in range(n):
    l1.append(int(input("enter number: ")))
for i in l1:
    sum+=i
print(sum)