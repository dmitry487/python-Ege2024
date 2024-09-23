kolichestvo = 0
counter = 0

for a1 in 'аинптця':
    for a2 in 'аинптця':
        for a3 in 'аинптця':
            for a4 in 'аинптця':
                for a5 in 'аинптця':
                    for a6 in 'аинптця':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        kolichestvo += 1
                        if a1 != 'н' and word.count('я') == 2 and kolichestvo%2 == 0:
                            counter += 1


print(counter)
