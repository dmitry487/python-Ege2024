def f(start, stop):
    if start == stop: return 0
    elif start > stop: return 1
    if start > 0:return f(start + 1, stop) + f(start * 1.5, stop)
print(f(1, 20))