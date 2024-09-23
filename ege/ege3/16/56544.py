def f(a, b):
    if a == 0: return 0
    if a > b: return f(a - 1, b) + b
    if a <= b: return f(a, b - 1) + a
    