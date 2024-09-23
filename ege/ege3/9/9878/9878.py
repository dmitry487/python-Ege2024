f = open('ege3/9/9878/9878.txt')


nums = [[int(i) for i in row.split()] for row in f]


def check(row):
    row = sorted(row)
    povtor= [] 
    for num in row:
        if row.count(num) > 1:
            povtor.append(num)
            
    if (
        (
            ((len(set(row))) == 5) and (len(povtor) == 3)
        )and
        (
            ((set(povtor)) != row[-1]) and (set(povtor) != row[0])
        )
    ):return IndexError(row)
    

k = 0
kolichestvo = 0
for row in nums:
        kolichestvo += 1
        if check(row):
            print(check(row))
            k += kolichestvo
            


print(k)


        
