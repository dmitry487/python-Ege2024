# for n in range (10, 10000):
#     n_bin = bin(n)[2:]
    

#     if n%2 == 0:
#         n_bin = n_bin[:-1]

#     else:

#         n_bin = '1' + n_bin
#         summa_2x = int(n_bin[-1]) + int(n_bin[-2])
#         n_bin += (bin(summa_2x))[2:]


#     r = int(n_bin, 2)

#     if r == 202:
#         print(n)
def perevod(num):
    n_troich = ''
    while num > 0:
        n_troich += str(num%3)
        num//= 3

            
    return n_troich[::-1]


for n in range(1, 100000):
    n = perevod(n)


    if sum([int(i) for i in n])%2 == 0:
        s = perevod(sum([int(i) for i in n]))
        n += str(s)

    else:
        n = '1' + n 
        m = perevod(int(n)%2)
        n += str(m)


    r = int(n, 3)

    if r > 1105:
        print(r)
        break

    
    

    

