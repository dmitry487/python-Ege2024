f = open('ege3/9/2/1.txt')


nums = [[int(i) for i in row.split()] for row in f]



def check(row):
    row = sorted(row)

    if (
        (
            ((row[0]) != (row[1])) and ((row[0]) != (row[2])) and\
            ((row[1]) != (row[2]))
        )and
        (
            ((row[0]) * (row[1]) * (row[2])) > ((row[-1]) ** 2)
        )
    ):return True
    return False

kolichetvo = 0


for row in nums:
    if check(row):
        kolichetvo += 1


print(kolichetvo)