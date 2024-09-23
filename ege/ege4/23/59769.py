def f(start, stop):
    if start == stop: return True
    elif start > stop or start == 6: return False
    return f(start + 1, stop) + f(start + 2, stop) + f(start * 2, stop)


print(f(4, 15) * f(15, 19))