for n in range(100, 1, -1):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    s = s[::-1]
    s = s[s.find('1'):]
    r = int(s, 2)  # перевод в десятичную систему
    if r == 13:
        print(n)
        break