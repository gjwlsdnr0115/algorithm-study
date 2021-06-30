m, n = map(int, input().split())
board = []
mini = []

for _ in range(m):
    board.append(input())

for i in range(m-7):
    for j in range(n-7):
        idx1 = 0
        idx2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2==0:
                    if board[k][l] != 'W':
                        idx1 += 1
                    if board[k][l] != 'B':
                        idx2 += 1
                else:
                    if board[k][l] != 'B':
                        idx1 += 1
                    if board[k][l] != 'W':
                        idx2 += 1
        mini.append(idx1)
        mini.append(idx2)

print(min(mini))