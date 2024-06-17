'''Write a python program that takes a list of numbers and returns their sum'''
n=int(input("enter length: "))
l1=[]

for i in range(0,n):
    a=int(input("enter no. "))
    l1.append(a)

list_sum=0
for i in range(n):
    list_sum+=l1[i]

print(list_sum)