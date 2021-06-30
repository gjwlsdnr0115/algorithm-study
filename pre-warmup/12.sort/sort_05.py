n_str = input()
nums = [int(c) for c in n_str]
nums.sort(reverse=True)
for num in nums:
    print(num, end='')