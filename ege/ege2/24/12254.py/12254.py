f = open('ege2/24/12254.py/24_12254.txt').read()


f = f.replace("RSQ", "___")


for i in range(1000, 0, -1):
    if '_'*i in f:
        max_len = i
        break

substring = max_len*"*"

f = f.replace("_" * max_len, substring)

vars = [
    "SQ" + substring + "RS",
    "SQ" + substring + "R",
    "Q" + substring + "RS",
    "Q" + substring + "R",
    ]


for var in vars:
    if var in f:
        print(len(var))
        break
