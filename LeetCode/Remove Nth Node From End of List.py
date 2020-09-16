# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        toRemove = head
        front = head
        for i in range(n+1):
            if not front:
                return head.next
            front = front.next
            
        while front:
            toRemove = toRemove.next
            front = front.next
        toRemove.next =  toRemove.next.next

        return head