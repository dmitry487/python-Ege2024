def check(num):

    deliteli = set()


    for i in range (2, int(num ** 0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)


        
    if len(deliteli) >= 5:
        return sorted(list(deliteli))
    
    else:
        return False
    


for num in range (460_000_000, 460_000_100):
    if check(num):
        print(check(num)[4])


#41818182
# 261959
# 5
# 271
# 57500001
