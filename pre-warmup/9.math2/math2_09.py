while True:
    nums = list(map(int, input().split()))
    if sum(nums)==0:
        break
    longest = max(nums)
    nums.remove(longest)

    if nums[0]**2 + nums[1]**2 == longest**2:
        print('right')
    else:
        print('wrong')