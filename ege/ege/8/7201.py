kolichestvo = 0
for a1 in 'внрт':
    for a2 in 'внрт':
        for a3 in 'внрт':
            for a4 in 'внрт':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                if kolichestvo == 250:
                    print(kolichestvo, word)
                
