


f = open('ege2/24/35913/24-4.txt').readlines()

min_kol = 10000

for posl in f:
    if posl.count('N') < min_kol:
        min_kol = posl.count('N')

for loh in f:
    if loh.count("N") == 23:
        print(set(loh))
        print((loh))
        print(loh.count('W'))
        print(loh.count('Q'))
        print(loh.count('R'))
        print(loh.count('M'))
        print(loh.count('J'))
        print(loh.count('L'))
        print(loh.count('N'))
        print(loh.count('V'))
        print(loh.count('H'))
        print(loh.count('Z'))
        print(loh.count('C'))
        print(loh.count('X'))
        print(loh.count('I'))
        print(loh.count('B'))
        print(loh.count('U'))
        print(loh.count('T'))
        print(loh.count('F'))
        print(loh.count('P'))
        print(loh.count('E'))
        print(loh.count('S'))
        print(loh.count('D'))
        print(loh.count('Y'))
        print(loh.count('G'))
        print(loh.count('O'))
        print(loh.count('A'))
        print(loh.count('K'))


