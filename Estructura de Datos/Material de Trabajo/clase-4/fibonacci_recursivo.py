def fibonacci_recursivo(n):
    if n <= 1:
        return n

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


print(fibonacci_recursivo(10))  # 55