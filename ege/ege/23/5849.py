def f(start, stop):
    if start == stop:return 1
    elif start > stop: return 0
    return f(start + 1, stop) + f(start + 10, stop)

print(f(35, 57))