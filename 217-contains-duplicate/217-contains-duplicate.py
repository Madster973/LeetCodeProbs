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
        return len(nums) != len(set(nums))
        
        