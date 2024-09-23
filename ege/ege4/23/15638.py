def f(start, stop):
    if start == stop: return True
    elif start > stop or start == 17: return False
    return f(start + 1, stop) + f(start * 2, stop)


print(f(1, 10) * f(10, 21))