n, limit = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(n):
    if nums[i] < limit:
        print(nums[i], end=' ')