f = open('ege3/9/46967/46967.txt')



nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    row = sorted(row)
    if (
        (
            ((row[0] + row[1]) < row[2]) or\
            ((row[0] + row[1]) < row[3]) 
            
        )
    ):return True
    return False


kolichestvo = 0



for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)