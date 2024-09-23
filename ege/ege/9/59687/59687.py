f = open('ege/9/59687/59687.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    povtor = []
    nepovtor = []
    for num in row:
        if (row.count(num) == 3) and (len(set(row)) == 4): return True
        return False
    
    
