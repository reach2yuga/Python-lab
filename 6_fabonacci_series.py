#fabonacci series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = 10  # Change this value to generate more or fewer terms
result = fibonacci(n)
print(f"The first {n} terms of the Fibonacci series are: {result}")