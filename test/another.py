# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    return fib_sequence
def hello():
    pass

result = hello()

b = int("donut")

def add(x, y):
    print(x + y)


value = add(10, 10)
# Attempt to generate 10 terms of the Fibonacci sequence
num_terms = 10
print(f"Fibonacci sequence with {num_terms} terms: {fibonacci(num_term)}")
