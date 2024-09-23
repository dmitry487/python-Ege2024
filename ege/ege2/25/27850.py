def check(num):
    
    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            return False
    
    return True
    
poryad = 0
for num in range (245690, 245756 + 1):
    poryad += 1
    if check(num):
        print(poryad, num)