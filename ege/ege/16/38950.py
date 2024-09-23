def f(n):
    if n == 0: return 0
    if n > 0 and (n%2 == 0): return f(n/2)
    return 1 + f(n - 1)


kolichestvo = 0


for n in range (1, 500 + 1):
    if f(n) == 8 :
        kolichestvo += 1


print(kolichestvo)
        