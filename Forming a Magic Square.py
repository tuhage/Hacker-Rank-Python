import math


def formingMagicSquare(s):

    corners = list([s[0][0], s[0][1], s[0][2], s[1][2], s[2][2], s[2][1], s[2][0], s[1][0]])

    liste = list([[4, 9, 2, 7, 6, 1, 8, 3], [4, 3, 8, 1, 6, 7, 2, 9], [2, 9, 4, 3, 8, 1, 6, 7], [2, 7, 6, 1, 8, 3, 4, 9],
                 [6, 1, 8, 3, 4, 9, 2, 7], [6, 7, 2, 9, 4, 3, 8, 1], [8, 3, 4, 9, 2, 7, 6, 1],
                 [8, 1, 6, 7, 2, 9, 4, 3]])
    min=1000
    for i in range(8):
        count=countreturn(corners,liste[i])
        if count < min :
            min=count

    if s[1][1] != 5:
        min += math.fabs(5 - s[1][1])

    return int(min)


def countreturn(corners, list):
    count = 0
    for i in range(8):
        count += math.fabs(corners[i] - list[i])
    return int(count)


print(formingMagicSquare([[4, 5, 8], [2, 4, 1], [1, 9, 7]]))

