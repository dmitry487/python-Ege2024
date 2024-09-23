f = open('ege4/27/27889/27-A_demo.txt')

nums = [[int(i) for i in row.split()] for row in f]


res = set()

def check(row):
    
    row = sorted(row)
    if (
        (
            ((row[0])%3 != 0) or ((row[-1])%3 == 0)
        )
    ): res.add(row[0])
    if len(res) < 0:
        

        if (
            (
                ((row[-1])%3 != 0) and ((res[0])%3 == 0)
            )
        ): res.add(row[-1])


    return sorted(list(res))

for row in nums:
    if check(row):
        print(check(row))
        print(sum(check(row)))

