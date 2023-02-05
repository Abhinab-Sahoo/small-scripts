# function to implement binary search
def binary_search(sequence, key):
    # set the lower bound of the search
    low = 0
    # set the upper bound of the search
    high = len(sequence) - 1

    # loop until the lower bound is greater than the upper bound
    while low <= high:
        # find the middle index
        mid = (low + high) // 2
        # check if the middle element matches the key
        if sequence[mid] == key:
            # return the index if the key is found
            return f"Key is on {mid}th index."
        # check if the key is greater than the middle element
        elif key > sequence[mid]:
            # update the lower bound if the key is greater than the middle element
            low = mid + 1
        else:
            # update the upper bound if the key is less than the middle element
            high = mid - 1

    # return "Item not in list" if the key is not found
    return "Item not in list"


# test the binary search function
sequence = [2, 5, 8, 10, 13, 27, 31, 34, 43, 57, 81]
key = 57
print(binary_search(sequence, key))
