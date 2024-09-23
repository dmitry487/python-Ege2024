def f(start, stop):
    if start == stop: return True
    elif start > stop or start == 16: return False
    return f(start + 1, stop) + f(start + 2, stop) + f(start * 3, stop)

print(f(2, 9) * f(9, 18))