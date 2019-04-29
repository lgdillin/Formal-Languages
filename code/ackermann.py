import sys
sys.setrecursionlimit(8000)

def A(x, y):

    # rule 1
    if x == 0 and y >= 0:
        return 1

    # rule 2
    if x == 1 and y == 0:
        return 2

    # rule 3
    if x >= 2 and y == 0:
        return x + 2

    # rule 4
    if x >= 0 and y >= 0:
        x = x - 1
        y = y - 1

        return A(A(x, y + 1), y)

    raise Exception('Something terrible happened!')

x = A(15, 2)
print(x)