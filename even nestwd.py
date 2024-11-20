#even
x=int(input("enter the :"))
if x%2==0:
    print("this number is even")
else:
    print("this number is add")
    #nestw
    # d
x=int(input("enter the first number"))
y=int(input("enter the 2ndt number"))
z=int(input("enter the 3rd number"))
if y>x:
    if y>z:
        print("y us max")
    else:
        print("c is max")
elif x>y:
    if x>z:
        print("x  is max")
    else:
        print("c is ma")
#even number by loops
num = 1
sum = 0
while num <= 10:
    if num % 2 == 0:
        sum += num
    num=num+1
print("The sum of even numbers from 1 to 10 is:", sum)
#odd number
num = 1
even_sum = 0


while num <= 10:
    if num % 2 != 0:  # Check if the r is even
        even_sum += num  # Add the even number to the sum
    num += 1  # Increment the number

print("The sum of even numbers from 1 to 10 is:", even_sum)
