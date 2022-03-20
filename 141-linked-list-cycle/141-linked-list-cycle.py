# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        note_dict = {}
        while head:
            if head in note_dict:
                return True
            else:
                note_dict[head] = 1
                head = head.next
        return False
        