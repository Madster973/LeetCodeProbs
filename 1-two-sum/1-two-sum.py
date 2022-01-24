class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_1 = {}
        for i in range(len(nums)):
            if (target-nums[i]) in dict_1:
                return [i,dict_1[target-nums[i]]]
            else:
                dict_1[nums[i]] = i
        return [-1,-1]