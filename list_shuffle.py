# program to shuffle elements of a list provided by the user

import random  # importing random to perform shuffle on it

num = int(input("Enter the number of elements in your list: "))  # user inputs desired length of the list
list1 = []

for x in range(num):
    x = int(input("element:"))  # To input elements by the user
    list1.append(x)

random.shuffle(list1)   # using shuffle method on the list
print(f"your list of elements: {list1}")

