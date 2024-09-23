def f(start, stop):
    if start == stop: return 1
    elif start > stop: return 0
    return f(start + 1, stop) + f(start * 2, stop)

def f1(start, stop):
    if start == stop: return 1
    elif start > stop: return 0
    return f(start + 1, stop) + f(start * 2, stop)


print(f(1,9) * f(9, 20) + f(1,10) * f(10, 20))