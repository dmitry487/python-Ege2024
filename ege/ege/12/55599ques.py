s = '0'+ 69 * '1' + 69 * '2' + '0'

while '00' not in s:
    s = s.replace('02', '101')
    s = s.replace('11', '2')
    s = s.replace('12', '21')
    s = s.replace('010', '00')
    print(s, s.count('1'))


