def f(n):
    def g(n):
        if n == 1: return 1
        if n > 1: return 2 * g(n - 1) + 5 * n
        if g == 1: return 1
        if n > 1: return f(n - 1) + 2 * n

print(f(4) + f(4))