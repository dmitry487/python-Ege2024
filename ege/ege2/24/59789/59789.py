f=open('ege2/24/59789/24-2.txt').readline()

f=f.split('Y')
max_len=0
for i in range(len(f)-100):
    st='Y'.join(f[i:i+101])
    if max_len < len(st):
        max_len=len(st)
print(max_len)
