"""
please input number:10
01 36 35 34 33 32 31 30 29 28
02 37 64 63 62 61 60 59 58 27
03 38 65 84 83 82 81 80 57 26
04 39 66 85 96 95 94 79 56 25
05 40 67 86 97 100 93 78 55 24
06 41 68 87 98 99 92 77 54 23
07 42 69 88 89 90 91 76 53 22
08 43 70 71 72 73 74 75 52 21
09 44 45 46 47 48 49 50 51 20
10 11 12 13 14 15 16 17 18 19
"""

size = int(input('please input number:'))
array = [[0] * size]
for i in range(size - 1):
    array += [[0] * size]

orient = 0
k = 0
j = 0
for i in range(1, size * size + 1):
    array[j][k] = i
    if k + j == size - 1:
        if j > k:
            orient = 1
        else:
            orient = 2
    elif (k == j) and (k >= size/2):
        orient = 3
    elif (j == k - 1) and (k <= size/2):
        orient = 0

    if orient == 0:
        j += 1
    elif orient == 1:
        k += 1
    elif orient == 2:
        k -= 1
    elif orient == 3:
        j -= 1

for i in range(size):
    for j in range(size):
        print('%02d ' % array[i][j], end='')
    print('')