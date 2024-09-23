def f(start, stop):
    if start == stop: return 1
    elif start > stop or start == 11:return 0
    return f(start + 1, stop) +\
    f(start * 2, stop) +f(start + 5, stop)

print(f(1,9) * f(9,18))