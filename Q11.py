'''Write a python program that generates the first n numbers in the
Fibonacci sequence.'''
a=int(input("enter number"))


fib1=1
fib0=0
print(fib0)
print(fib1)

for i in range(2,a+1):
    fib = fib1 + fib0
    print(fib," ")
    fib0=fib1
    fib1=fib

