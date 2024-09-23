f = open('ege4/24/16388/24_16388.txt').read()



for i in range (200, 0, -1):
    if 'KLMN' * i in f:
        s = i * 'KLMN'
        break


vars_l = ['LMN', 'MN', 'N', '']
vars_r = ['KLM', 'KL', 'K', '']

for var_l in vars_l:
    for var_r in vars_r:
        sub_s = var_l + s + var_r

        if sub_s in f:
            print(len(sub_s))