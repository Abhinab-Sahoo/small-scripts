# function to print FizzBuzz sequence
def main():
    # loop through the numbers from 1 to 100
    for i in range(1, 101):
        # check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            # print "FizzBuzz" if the number is divisible by both 3 and 5
            print("FizzBuzz")
        # check if the number is divisible by 3
        elif i % 3 == 0:
            # print "Fizz" if the number is divisible by 3
            print("Fizz")
        # check if the number is divisible by 5
        elif i % 5 == 0:
            # print "Buzz" if the number is divisible by 5
            print("Buzz")
        else:
            # print the number if it's not divisible by either 3 or 5
            print(i)

# check if the script is being run as the main module
if __name__ == "__main__":
    # call the main function if the script is being run as the main module
    main()