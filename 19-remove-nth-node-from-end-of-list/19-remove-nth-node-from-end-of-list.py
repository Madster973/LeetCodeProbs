# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Assigning two pointers slow and fast
        slow=fast=head
        # Incrementing the fast pointer by the times the index of the node to be deleted
        for i in range(n):
            fast = fast.next
        # After incrementing the fast node if it is none it means that there are only 
        # 1 or 2 values in the array and we are deleting the first 1
        # Example [1,2] 1 or [1] 1
        if not fast:
            return head.next
        # Increment the fast and slow simultaneously, by the time the fast reaches end the slow
        # would be at the pointer where we need to delete the node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
    