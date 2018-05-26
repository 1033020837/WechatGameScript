dic = {
    0:[0,1,0,2,0,2,2,1,2],
    1:[0,0,0,0,0,2,0,0,2],
    2:[0,1,0,0,1,2,2,1,0],
    3:[0,1,0,0,1,2,0,1,2],
    4:[0,0,0,2,1,2,0,0,2],
    5:[0,1,0,2,1,0,0,1,2],
    6:[0,1,0,2,1,0,2,1,2],
    7:[0,1,0,0,0,2,0,0,2],
    8:[0,1,0,2,1,2,2,1,2],
    9:[0,1,0,2,1,2,0,0,2]
}

def printLine(line):
    index = 0
    for l in line:
        if l == 0:
            print('.', end='')
        elif l == 1:
            print('_', end='')
        else:
            print('|', end='')
        if index % 3 == 2:
            print(' ', end='')
        index += 1
    print()

def printDigit(digits):
    res = []
    for digit in str(digits):
        res.append(dic[int(digit)])
    lines = [[],[],[]]
    for r in res:
        lines[0].extend(r[0:3])
        lines[1].extend(r[3:6])
        lines[2].extend(r[6:9])
    for line in lines:
        printLine(line)

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    printDigit(n)