res = []
for i in range (600, 999):
    s = 0
    i_str = str(i)

    sum_cifri = int(i_str[0]) + int(i_str[1]) + int(i_str[2])
    
    s = (i - int(sum_cifri))//3

    res.append(s)
    

print(len(set(res)))

   
