
def trey(n,m,k):
    naim = min(n, m, k)
    naib = max(n, m, k)
    sr = ((n + m + k) - naim - naib)
    return naim + sr > naib

for a in range (1000, 1, -1):
    flag = True

    for x in range (1000):
        if not (
            (trey(a,5,x)) <=\
            ((max(x,11) < 19) == (not(trey(23,13,x))))
        ): flag = False
    
    if flag:
        print(a)
        break