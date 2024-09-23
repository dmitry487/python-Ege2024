def f(n):
    if n == 0: return 1
    if n%2 == 1: return (n%10) * f(n//100)
    if n > 0 and n%2 == 0: return f(n//100)

kolichestvo = 0
for n in range (10 ** 7, 8 * 10 ** 7 + 1):
    if f(n) == 35:
        kolichestvo += 1


print(kolichestvo)