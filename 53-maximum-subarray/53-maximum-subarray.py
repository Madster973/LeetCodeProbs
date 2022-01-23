class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        from sys import maxsize
To Track indexes of start and end
def maxSubArraySum(a, size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            # in case of negative numbers we are making max_ending_here = 0
            # because if we encounter a positive integer we would be starting the train from there not from negative
            print(max_ending_here)
            max_ending_here = 0
            s = i + 1
            print(s)

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))
a = [-1,-2,-3,4]
maxSubArraySum(a,len(a))
        """
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            cur_sum = max(nums[i],nums[i]+cur_sum)
            max_sum = max(cur_sum,max_sum)
        return max_sum
    