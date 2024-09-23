def f(start, stop):
    if start == stop: return True
    elif start > stop: return False

    return f(start + 1, stop) + f(start + 2, stop) + f(start * 2, stop)



print(f(3, 10) * f(10, 12))