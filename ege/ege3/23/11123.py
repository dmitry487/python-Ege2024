def f(start, stop):
    if start == stop: return True
    elif start < stop: return False
    return f(start - 2, stop) + f(start - 5, stop)


print(f(22, 2))