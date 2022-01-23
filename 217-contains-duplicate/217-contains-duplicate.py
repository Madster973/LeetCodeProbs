class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        hash_table = []
        for i in nums:
            if i in hash_table:
                return True
            else:
                hash_table.append(i)
        return False
        Time Limit exceeded
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
        