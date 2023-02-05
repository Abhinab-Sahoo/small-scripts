# function to check if a string is a palindrome
def is_palindrome(N):
    # convert the string to lowercase and remove leading/trailing whitespaces
    N = N.lower().strip()
    # return True if the string is a palindrome, False otherwise
    return N == N[::-1]

# get the input string from the user
input_string = input("Input for palindrome: ")

# check if the input string is a palindrome
if is_palindrome(input_string):
    # print that the string is a palindrome
    print(f"{input_string} is palindrome")
else:
    # print that the string is not a palindrome
    print(f"{input_string} is not a palindrome")