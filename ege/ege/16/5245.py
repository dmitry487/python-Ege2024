def f(n):
    if n == 1: return 1
    if n == 2: return 2
    return 3 * f(n - 1) - 2 * f(n - 2)

print(f(7))