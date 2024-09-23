def check(num):
    deliteli = set()

    for i in range (1, int(num ** 0.5) + 1):
        if num%i == 0:
            
            deliteli.add(i)
            deliteli.add(num//i)

    return len(deliteli)
# max_len = 0
# for num in range (84052, 84130 + 1):
#     max_len = max(max_len, check(num))
#     if check(num) == max_len:
#         print(num, max_len)

res = []

for num in range (84052, 84130 + 1):
    res.append([check(num), num])

print(sorted(res))