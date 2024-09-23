for n in range (100, 1000):
    n_str = str(n)
    res =   n_str[0] + str(int(n_str[0]) + int(n_str[1])) +\
          n_str[1] + str(int(n_str[1]) + int(n_str[2])) + n_str[2]
    
    if int(res)%11 == 0:
        print(res)