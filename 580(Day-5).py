# Task 1: Ask the user to enter a positive integer n
n = int(input("Enter a positive integer: "))

# Task 2: Use a for loop to print all numbers from 1 to n on separate lines
print("Numbers from 1 to", n, "using a for loop:")
for i in range(1, n + 1):
    print(i)

# Task 3: Use a while loop to calculate the sum of all numbers from 1 to n
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1

print(f"The sum of all numbers from 1 to {n} is:", sum_of_numbers)
