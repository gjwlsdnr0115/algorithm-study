def hanoi_tower(n, start, finish):
    if n==1:
        print(start, finish)
        return

    hanoi_tower(n-1, start, 6-start-finish)
    print(start, finish)
    hanoi_tower(n-1, 6-start-finish, finish)


n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)