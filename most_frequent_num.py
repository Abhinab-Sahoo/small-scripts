# function to find the most frequent element in a list
def most_frequent(n):
    # dictionary to store the count of each element in the list
    count = {}
    # iterate over the elements in the list
    for i in n:
        # if the element is already in the dictionary, increment its count by 1
        if i in count:
            count[i] += 1
        # if the element is not in the dictionary, add it and set its count to 1
        else:
            count[i] = 1
    # return the element with the highest count
    return max(count, key=count.get)

# sample list of integers
n = [1, 2, 3, 4, 3, 4, 7, 1]
# find the most frequent element in the list and print it
print(f"Most frequent number is {most_frequent(n)}")
