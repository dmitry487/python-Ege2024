def f(n):
    if n > 100_0000: return n
    if n <= 1000000: return n + f(2 * n)

def g(n):
    return f(n)/n


kolichestvo = 0
g_ = g(1000)
for n in range (1, 10000):
    if g(n) == g_:
        kolichestvo += 1

print(kolichestvo)
