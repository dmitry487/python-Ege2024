kolichestvo = 0
for a1 in 'уоа':
    for a2 in 'уоа':
        for a3 in 'уоа':
            for a4 in 'уоа':
                for a5 in 'уоа':
                    for a6 in 'уоа':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        kolichestvo += 1

                        if word == 'оуууоо':
                            print(kolichestvo)