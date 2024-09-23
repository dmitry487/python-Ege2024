def f(start, stop, asd):
    if start == stop: 
        return 1
    if start - 1 > stop: 
        return 0
    if asd == 0:
        return f(start * 2, stop, 0) + f(start * 3, stop, 0) + f(start - 1, stop, asd + 1)
    else:
        return f(start * 2, stop, 0) + f(start * 3, stop, 0)
print(f(3, 20, 0))