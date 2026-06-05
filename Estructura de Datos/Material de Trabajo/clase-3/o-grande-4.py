def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Llamadas recursivas
    return fibonacci(n - 1) + fibonacci(n - 2)


