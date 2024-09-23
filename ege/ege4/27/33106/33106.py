f = open('ege4/27/33106/dsdfsdf.txt')

nums = [[int(i) for i in row.split()] for row in f]

res = []

def check(row):
    row = sorted(row)
    
    res.append(row[0])

    return sorted(list(res))

