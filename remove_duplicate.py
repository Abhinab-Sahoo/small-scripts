# code to remove duplicates from a list

# initialize the input list
N = [2, 4, 9, 23, 14, 5, 4, 19, 3, 6, 9]

# initialize an empty list to store the unique elements
output = []

# loop through the input list
for i in N:
    # check if the current element is not in the output list
    if i not in output:
        # if the element is not in the output list, add it
        output.append(i)

# sort the output list and print the result
print(sorted(output))