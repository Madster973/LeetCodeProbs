class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        nums1 = [0]*len(nums)
        k = len(nums)-1
        while left<=right:
            if abs(nums[left])<=abs(nums[right]):
                nums1[k] = nums[right]**2
                right = right-1
            else:
                nums1[k] = nums[left]**2
                left = left+1
            k = k-1
        return nums1
                
        