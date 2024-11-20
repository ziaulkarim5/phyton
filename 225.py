# Sum of even numbers from 1 to 10
num = 1
even_sum = 0
while num <= 10:
    if num % 2 == 0:
        even_sum += num
    num=num+ 1  # Increment the number to avoid an infinite loop

print("The sum of even numbers from 1 to 10 is:", even_sum)

# Sum of odd numbers from 1 to 10
num = 1
odd_sum = 0

while num <= 10:
    if num % 2 != 0:  # Check if the number is odd
        odd_sum += num  # Add the odd number to the sum
    num += 1  # Increment the number

print("The sum of odd numbers from 1 to 10 is:", odd_sum)
