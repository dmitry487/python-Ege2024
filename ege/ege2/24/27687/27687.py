f = open('ege2/24/27687/24_demo.txt').read()


f = f.replace("X", " ")
f = f.replace("Z", " ")
f = f.replace("Y", "_")
f = f.split()
print(f)

max_posl = 0


for posl in f:
    max_posl = max(max_posl, len(posl))

print(max_posl)