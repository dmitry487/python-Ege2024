kolichestvo = 0


bad_sluchai = []


for i in 'ааббввгг':
        bad_sluchai.append(i + i)
        print(bad_sluchai)


def check(word):
    if (
        (str(word)[0] != 'а') and
        (word not in bad_sluchai)
        ): return True
    return False

for a1 in 'абвг':
      for a2 in 'абвг':
            for a3 in 'абвг':
                  for a4 in 'абвг':
                        for a5 in 'абвг':
                              for a6 in 'абвг':
                                    word = a1 + a2 + a3 + a4 + a5 + a6
                                    if check(word):
                                          kolichestvo += 1

print(kolichestvo)

