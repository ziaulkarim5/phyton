while True:
       print("1. Addition")
       print("2. Subtraction")
       print("3. Multiplication")
       print("4. Division")
       print("5. Exit")
       CHOICE=int(input("Enter your choice:"))
       if CHOICE==1:
          x =int(input("Enter your first number:"))
          y=int(input("Enter your second number:"))
          print("sum =",x+y)
       elif CHOICE==2:
          x =int(input("Enter your first number"))
          y=int(input("Enter your second number"))
          print("sub =", x - y)
       elif CHOICE==3:
          x =int(input("Enter your first number"))
          y=int(input("Enter your second number"))
          print("multy =", x * y)
       elif CHOICE==4:
          x =int(input("Enter your first number"))
          y=int(input("Enter your second number"))
          print("division =", x / y)
       elif CHOICE==5:
          break
       else:
          print("invalid")