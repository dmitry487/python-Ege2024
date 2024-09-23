f = open('ege/9/51978/51978.txt')


nums = [[int(i) for i in row.split()] for row in f]

def f(row):
    for (num1, num2, num3, num4, num5) in row:
        nechet = []
        chet = []
        if (
            (
                (len(set(row))) == 5
            )and 
            (
                num1 % 2 !=0
            )
        ):return True
        return False