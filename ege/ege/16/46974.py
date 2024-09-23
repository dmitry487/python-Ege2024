def f(n):
    if n == 0: return 0
    if n%2!= 0: return f(n - 1) + 1
    if n > 0 and n%2 == 0: return f(n/2)
kolichestvo = 0

for n in range (1, 1000000000):
    if f(n) == 2:
        kolichestvo += 1
    
print(kolichestvo)