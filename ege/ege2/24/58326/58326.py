f = open('ege2/24/58326/24_5832.txt').read()

for i in range(0, 10):
    f = f.replace(str(i) + '1', ' ')
    
    f = f.replace(str(i) + '2', ' ')
    
    f = f.replace(str(i) + '3', ' ')
    
    f = f.replace(str(i) + '4', ' ')
    
    f = f.replace(str(i) + '5', ' ')
    
    f = f.replace(str(i) + '6', ' ')
    
    f = f.replace(str(i) + '7', ' ')
    
    f = f.replace(str(i) + '8', ' ')
    
    f = f.replace(str(i) + '9', ' ')
    i += 1

f = f.split()

max_ = 0
super_max = 0
for posl in f:
    max_ = len(posl)
    super_max = max(max_, super_max)

print(super_max)
    
