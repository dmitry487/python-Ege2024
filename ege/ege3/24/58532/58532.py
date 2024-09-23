f = open("ege3/24/58532/24-10.txt").read()
f = "BADZXYZKLMENYZXXX"
letters = list(f)

def check(triplet: str):
    return triplet.count("X") == triplet.count("Y") == triplet.count("Z") == 1

checkList = [0]*len(letters)


for i in range(len(letters) - 2):
    subString = letters[i:i + 3]
    if check(subString):
        checkList[i:i + 3] = [1]*3
        print(checkList)
        

result = ""

for i in range(len(letters)):
    if checkList[i] == 1: result += ' '
    else: result += letters[i]


print(max(
    [len(i) for i in result.split()]
))