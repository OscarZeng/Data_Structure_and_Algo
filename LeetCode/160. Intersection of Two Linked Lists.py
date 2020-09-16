# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        pa, pb = headA, headB
        while pa != pb:
            if pa == None:
                pa = headB
            else:
                pa = pa.next
            if pb == None:
                pb = headA
            else:
                pb = pb.next
        return pa