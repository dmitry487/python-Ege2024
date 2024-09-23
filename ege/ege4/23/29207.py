def f(start, stop):
    if start == stop: return True
    elif start > stop  or start == 12: return False
    return f(start + 1, stop) + f(start * 2, stop)

def g(start, stop):
    if start == stop: return True
    elif start > stop or start == 11:return False
    return g(start + 1, stop) + g(start * 2, stop)

print((f(2, 11) * f(11, 24)) + (g(2, 12) * g(12, 24)))