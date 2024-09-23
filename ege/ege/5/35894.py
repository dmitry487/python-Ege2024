for n in range (105, 1000):
    n_bin = bin(n)[2:]
    kolvo_ed = n_bin.count('1')
    kolvo_nul = n_bin.count('0')
    if kolvo_ed == kolvo_nul:
        n_bin += n_bin[-1]
    elif kolvo_ed > kolvo_nul:
        n_bin += n_bin + '0'
    else:
        n_bin += n_bin + '1'
    if kolvo_ed == kolvo_nul:
        n_bin += n_bin[-1]
    elif kolvo_ed > kolvo_nul:
        n_bin += n_bin + '0'
    else:
        n_bin += n_bin + '1'
    if kolvo_ed == kolvo_nul:
        n_bin += n_bin[-1]
    elif kolvo_ed > kolvo_nul:
        n_bin += n_bin + '0'
    else:
        n_bin += n_bin + '1'
    r = int(n_bin, 2)
    if r%4==0:
        print(n)
        break