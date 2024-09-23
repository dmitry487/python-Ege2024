kolichestvo = 0
bad_combos = 'ае'

def check(word):
    for combos in word:
        if bad_combos in combos: return False
        return True
    
word = 'праевет'

if check(word):
    print('всё ок')
else: 
    print('net')