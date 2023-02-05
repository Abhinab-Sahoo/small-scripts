# define two lists - keys and values
key = ["a", "b", "c"]
value = [1, 2, 3]

# create a dictionary from the two lists using the zip function
output_dict = dict(zip(key, value))

# print the resulting dictionary
print(output_dict)