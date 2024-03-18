print("This is an exponent calculator.")
number1 = float(input("Please enter your first number: "))
number2 = float(input("Please enter your second number: "))



print(number1 ** number2)

print("1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5")

print("This will")

def between():
    num1 = input("Enter your first number (Smallest number): ")
    num1 = int(num1)
    num2 = input("Enter your first number(Biggest number): ")
    num2 = int(num2)

    for num in range(num1, num2 + 1):
        print(num)

        
between()

def primes():
    x = input("Enter your first number(Smallest number): ")
    x = int(x)
    y = input("Enter your second number(Biggest number): ")
    y = int(y)
    for num in range(x, y):
        if num % 2 != 0:
            print(num)
            continue

print()

primes()

def factnumber():

    x = input("Enter your number: ")

    
 
    
    