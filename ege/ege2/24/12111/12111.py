f = open('ege2/24/12111/24_12111.txt').read()


f = f.replace('NYN', '_')
f = f.replace("HPY", "_")
f = f.replace('H', ' ')
f = f.replace("P", " ")
f = f.replace("N", " ")
f = f.replace("Y", " ")

f = f.split()
print(f)
max_vsego = 0
for posl in f:
    max_vsego = max(max_vsego, len(posl))


print(max_vsego)

#vsego 16 #HPY - 7 #NYN - 7
