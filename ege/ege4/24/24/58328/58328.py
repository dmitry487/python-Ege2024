f = open('ege4/24/24/58328/24_58328.txt').read()


# f = f.replace('00', ' ')
# f = f.replace('11', ' ')
# f = f.replace('22', ' ')
# f = f.replace('33', ' ')
# f = f.replace('44', ' ')
# f = f.replace('55', ' ')
# f = f.replace('66', ' ')
# f = f.replace('77', ' ')
f = f.replace('88', ' ')
f = f.replace('99', ' ')
f = f.split()

#9701267092987626908659896798506787090906952587057071512752302195820163080650267878575356


for posl in f:
    if '9701267092987626908659896798506787090906952587057071512752302195820163080650267878575356' in posl:
        print(posl)
    
