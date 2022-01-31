class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_table = {} 
        nums3 = []
        for i in nums1:
            if i in hash_table:
                hash_table[i]+=1
            else:
                hash_table[i]=1
        for j in nums2:
            if j in hash_table and hash_table[j]>0:
                nums3.append(j)
                hash_table[j]-=1
        return nums3
                
        