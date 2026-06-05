def cuenta_regresiva(n):
    if n == 0:
        print("Despegue!")
        return

    print(n)
    cuenta_regresiva(n - 1)