# function to flatten a 2D list into a 1D list
def main(N):
    # empty list to store the flattened 1D list
    output = []
    # iterate over the rows in the 2D list
    for i in N:
        # iterate over the elements in each row
        for j in i:
            # append each element to the output list
            output.append(j)
    # print the output list
    print(output)

# sample 2D list
N = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# call the main function and pass the sample 2D list as input
main(N)