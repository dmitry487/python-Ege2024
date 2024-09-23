kolichestvo = 0
for a1 in 'авеикнор':
    for a2 in 'авеикнор':
        for a3 in 'авеикнор':
            word = a1 + a2 + a3
            if word.count('в') == 1:
                kolichestvo += 1
            if word.count('а') == 0:
                print(kolichestvo, word)