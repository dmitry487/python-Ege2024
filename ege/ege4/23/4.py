def f(start, stop):
    if start == stop: return True
    elif start < stop: return False
    return f(start - int(str(start ** 2)[0]), stop) + f(start - (int(str(start[0])) + int(str(start[1]))), stop)


print(f(32, 1))