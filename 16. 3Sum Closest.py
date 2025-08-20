class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest= nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                curr_sum=nums[left]+nums[right]+nums[i]
                if abs(target-curr_sum)<abs(target-closest):
                    closest=curr_sum
                if curr_sum == target:
                    return target
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest