import sys
input = sys.stdin.readline

def count(arr):
    size = len(arr)
    result = 1

    for i in range(size):
        cnt = 1
        for j in range(1, size):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt

        cnt = 1
        for j in range(1, size):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt

    return result




N = int(input())

board = []
for _ in range(N):
    board.append([c for c in input().strip()])

ans = 0
for i in range(N):
    for j in range(N):

        if j > 0:
            board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
            result = count(board)
            if result > ans:
                ans = result
            board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]

        if i > 0:
            board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
            result = count(board)
            if result > ans:
                ans = result
            board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
print(ans)