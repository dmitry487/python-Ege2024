kolichestvo = 0
for a1 in '12345678':
    for a2 in '012345678':
        for a3 in '012345678':
            for a4 in '012345678':
                for a5 in '012345678':
                    if a1 > a2 and a2 > a3 and a3 > a4 and a4 > a5:
                        kolichestvo += 1

print(kolichestvo)