'''Write a python program that calculates the sum of the digits of a given
number.'''
num=int(input("enter number: "))
sum=0
while(num!=0):
    sum+=num%10
    num=int(num/10)
print(sum)