'''Write a program that reads data from a CSV file and prints it to the
console'''
file= open('data.csv', 'r')
for line in file:
    print(line.strip())