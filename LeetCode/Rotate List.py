# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        # if k == 0:
        #     return head
        tailOld = head
        length = 1
        #find the current tail
        while(tailOld.next):
            tailOld = tailOld.next
            length += 1
        tailOld.next = head
        
        tailNew = head
        for i in range(length-1-k%length):
            tailNew = tailNew.next

        Newhead = tailNew.next
        #When tailOld and tailNew points to the same node, there will be problems
        #tailOld.next = head
        tailNew.next = None
        return Newhead