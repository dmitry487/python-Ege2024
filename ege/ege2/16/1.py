

def f(n):
    if n == 0: return 1
    if n%2 == 0: return (n%10) * f(n//100)
    if n > 0 and n%2 == 0: return f(n//100)
kolichestvo = 0
for k in range (10 ** 7, 9 * 10 ** 7):
    if f(k) == 25:
        kolichestvo += 1
    
print(kolichestvo)
