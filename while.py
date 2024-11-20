while True:
    print("1.sum")
    print("2.sub")
    print("3.multy")
    print("4.div")
    x = int(input("enter the operatioon"))
    if x == 1:
        num1 = int(input("enter the first number"))
        num2 = int(input("nter the first number"))
        print(num1 + num2)
    elif x == 2:
        num1 = int(input("enter the first number"))
        num2 = int(input("nter the first number"))
        print(num1 - num2)
    elif x == 3:
        num1 = int(input("enter the first number"))
        num2 = int(input("nter the first number"))
        print(num1 * num2)
    elif x == 4:
        num1 = int(input("enter the first number"))
        num2 = int(input("nter the first number"))
        print(num1 / num2)
    elif x == 5:
        break
    else:
        print("invalid")