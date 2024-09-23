f = open('ege2/10/59782/59782.txt').read()

kolichestvo = 0
for i in '.,:!?-':
    f = f.replace(i, ' ')
for word in f.lower().split():
    if ('мой' in word) and (len(word) > 3):
        kolichestvo += 1
        print(word)

print(kolichestvo)