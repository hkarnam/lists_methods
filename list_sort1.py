# Write a Python program to sort a list in ascending order using loop.
# Input:- [100,10,1,298,65,483,49876,2,80,9,9213]
# Output:- [1,2,9,10,65,80,100,298,483,9213,49876]


# using a second list to store the minimum values of list
Input = [100,10,1,298,65,483,49876,2,80,9,9213]
Output = [] # initializing an empty list to add the sorted elements in order

for x in range(len(Input)):  # setting the empty list to be same length as the list to be sorted
    y = min(Input)    # getting the minimum of Input list
    Output.append(y)   # appending to the new sorted list
    Input.remove(y) # the minimum number is now removed to get the next minimum number

print(Output)