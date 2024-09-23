from string import digits, ascii_lowercase


alph = digits, ascii_lowercase[:6]


for x in alph:
        res = ('1' + x + 'bad', 16) + ('2' + 'c' + x + 'fe', 16)

        
        
print(res/15)