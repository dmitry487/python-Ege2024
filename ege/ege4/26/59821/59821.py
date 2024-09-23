f = open('ege4/26/59821/26_59821.txt')


kolvo_det = 994


shlif = []
okr = []

for i in range (1, kolvo_det + 1):
    vr_sl, vr_okr = [int(i) for i in f.readline().split()]
    

    if vr_sl < vr_okr:
        shlif.append([vr_sl, i])
    else:
        okr.append([vr_okr, i])

shlif = sorted(shlif)
okr = sorted(okr)
print(len(shlif) - 1)

#otvet - 448, 515