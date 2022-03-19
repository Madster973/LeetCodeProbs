# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        temp = head
        while temp is not None:
            count+=1
            temp = temp.next
        if count%2 == 0:
            mid = count/2 + 1
        else:
            mid = (count+1)/2
        for _ in range(1,mid):
            head = head.next
        return head
        