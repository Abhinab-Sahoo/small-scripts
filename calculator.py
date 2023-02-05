def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")



print("A. Adition")
print("S. Substaction")
print("M. Multipication")
print("D. Division") 
print("E. Exit")

choice = input("Enter Your Choice: ").lower()

if choice == "a":
    print("Adition")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    add(a, b)
elif choice == "s":
    print("Substaction")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    sub(a, b)
elif choice == "m":
    print("Multiplication")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    mul(a, b)
elif choice == "d":
    print("Division")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    div(a, b)
elif choice == "e":
    print("Program Ended!")
    quit()
