# Fibonacci Sequence Generator

def fibonacci(n):
    sequence = [0, 1]  # Start with the first two numbers
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence

# Ask the user for input
num = int(input("Enter the number of Fibonacci terms you want: "))
if num <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Sequence:", fibonacci(num))