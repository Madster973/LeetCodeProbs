class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Sliding window approach
        # total = 0
        # max_total = nums[0]
        # for i in nums:
        #     if total<0:
        #         total = 0
        #     total+=i
        #     max_total = max(total,max_total)
        # return max_total
        # DP Approach
        max_total = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i]+nums[i-1])
            max_total = max(max_total,nums[i])
        return max_total
            
