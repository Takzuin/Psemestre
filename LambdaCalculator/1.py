def factorial_normal(n):
    r = 1
    i = 2

    while i <= n:
        print(f'antes r: {r}')
        print(f'antes i: {i}')
        r *= i
        i += 1
        print(f'r: {r}')
        print(f'i: {i}')
    return r


factorial_normal(5)