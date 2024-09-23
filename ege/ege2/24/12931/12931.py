f = open('ege2/24/12931/24_12931.txt').read()

f = f.replace("VWXYZ", "_____")
f = f.replace("WXYZ", "____")
f = f.replace("XYZ", "___")
f = f.replace("YZ", "__")
f = f.replace("Z", "_")
f = f.replace("VWXY", "____")
f = f.replace("VWX", "___")
f = f.replace("VW", "__")
f = f.replace("V", "_")
f = f.replace("T", " ")
f = f.replace("U", " ")

f = f.split()

max_posl = 0

for posl in f:
    max_posl = max(max_posl, posl.count('_'))

print(max_posl)

# VWXYZ
# T, U, V, W, X, Y и Z