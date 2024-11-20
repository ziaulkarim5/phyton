
    #calty

print("1.sum")
print("2.sub")
print("3.multy")
print("4.divide")
option=int(input("enter the operation:"))
if option in [1,2,3,4] :
    num1=float(input("enter the fist number"))
    num2=float(input("enter the secound number"))
    if option==1:
       sum=num1+num2
       print("your answer is",sum)
    elif option==2:
      sub=num1-num2
      print("your answer is;", sub)

    elif option==3:
         multy=num1*num2
         print("your answer is", multy)
    elif option==4:


        div=num1/num2
        print("your answer is", div)

else:
    print("your input is invalid")




