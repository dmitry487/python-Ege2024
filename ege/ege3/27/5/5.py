f = open("ege3/27/5/inf_22_10_20_27a.txt")

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    row = sorted(row)
    
    return list(row)

res = 0
for row in nums:
    if check(row):
        if row[0] < row[1]:
            res += row[0]
        else:
            res+= row[1]

        

        if res%3 == 0:  
            print(res)