def f(n):
    if n == 0: return 0
    if n > 0 and n%2 == 0: return f(n / 2)
    return 1 + f(n - 1)

for n in range (10 ** 5):
    if f(n) == 12:
        print(n)
        break