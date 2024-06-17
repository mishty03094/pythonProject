'''Write a python program that counts the occurrences of a specific element
in a list'''

user_list = input("Please enter the elements of the list separated by spaces: ").split()
print(user_list)


element_to_count = input("Please enter the element to count: ")


count = 0


for element in user_list:
    if element == element_to_count:
        count += 1


print(element_to_count," occurances: ", count)
