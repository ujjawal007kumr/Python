def minimum_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = [float('inf')] * n
    jumps[0] = 0

    for i in range(1,n):
        for j in range(i):
            if j + nums[j] >= i:
                jumps[i] = min(jumps[i],jumps[j] + 1)
                break

    return jumps[n-1]

nums = [2,3,1,1,4]
result = minimum_jumps(nums)
print("minimum number of jumps:",result)