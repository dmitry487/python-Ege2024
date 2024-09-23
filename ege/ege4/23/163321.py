def f(start, stop):
    if start == stop: return True
    elif start > stop: return False
    return f(start + 1, stop) + f(start + 2, stop) + f(start * 2, stop)


print(f(4, 11) * f(11, 13) * f(13, 15))
 