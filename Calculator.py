
while True:
    firstNum = float(input("Please enter the first number: "))
    secondNum = float(input("Please enter the second number: "))
    operator = input("Please enter your operator: ")



    if operator == '+':
        print(str(firstNum + secondNum))
    elif operator == '-':
        print(str(firstNum - secondNum))
        if secondNum != 0:
            print(str(firstNum / secondNum))

        else:
           print("The second number cannot be 0")

    elif operator == '*':
        print(firstNum * secondNum)
    else:
        print("ERROR!")
        exit()

