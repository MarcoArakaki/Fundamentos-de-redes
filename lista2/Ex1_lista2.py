def pot(base, expoente):
    for i in range (1, expoente + 1):
        res = base ** i
        print(f"{base} elevado a {i} = {res}")
pot (2,5)