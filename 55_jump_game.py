def canJump(nums):
    maxReach = 0  # The furthest index we can reach

    for i in range(len(nums)):
        if i > maxReach:
            # We're stuck before reaching this index
            return False
        maxReach = max(maxReach, i + nums[i])

    return True
