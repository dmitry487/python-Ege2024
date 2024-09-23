kolichestvo = 0
for a1 in 'авест':
    for a2 in 'авест':
        for a3 in 'авест':
            for a4 in 'авест':
                for a5 in 'авест':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1
                    if word == 'света':
                        print(word, kolichestvo)
