# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Assign two pointers to head
        l1,l2 = headA,headB
        # Run the loop till both l1 and l2 are not equal
        while l1!=l2:
            # iterate through the linked list and if it reaches end jump to the head of other 
            # Linkedlist
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        # In case if they don't meet they would be returning None because the 
        # intersect at None
        return l1            

        