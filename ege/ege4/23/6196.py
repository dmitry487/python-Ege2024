def f(start, stop):
    if start == stop: return True
    elif start > stop: return False
    return f(start + 1, stop) + f(start + 3, stop)


print(f(22, 35))