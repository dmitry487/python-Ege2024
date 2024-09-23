f = open('ege4/9/12241/12241.txt')


nums = [[int(i) for i in row.split()] for row in f]



def check(row):
    povtor = []
    nepovtor =[]
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)

        if row.count(num) == 2:
            povtor.append(num)
    povtor = sorted(povtor)
    if (
        (
            (len(nepovtor ) == 1) and ((len(povtor)) == 6) and 
            ((len(set(povtor))) == 3)
        )and
        (
            ((povtor[-1] + povtor[0])//2) < (sum(nepovtor))
        )
    ):return True
    return False


kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)