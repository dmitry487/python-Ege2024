# def check(num):

#     deliteli = set()


#     for i in range (1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             if i%2 == 0:
#                 deliteli.add(i)
#             if num//i%2 == 0:
#                 deliteli.add(num//i)

#     if len(deliteli) == 5:
#         return True
#     return False


# for num in range (35_000_000, 40_000_000 + 1):
#     if check(num):
#         print(num)


# является ли число простым
def prime(n:int):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True


def del_na_2(n):
    while n%2 == 0:
        n //= 2
    return n


for i in range(35_000_000, 40_000_000 + 1):
    tmp = del_na_2(i)
    if (
        (tmp**0.25) == int(tmp**0.25) and
        prime(tmp**0.25)
    ):
        print(i)