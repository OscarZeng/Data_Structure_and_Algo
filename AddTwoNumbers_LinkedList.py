# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #initiate the linked list
        ans = ListNode(0)
        startpoint = ans
        toadd = 0
        while(l1 or l2):
            #Classic way of checking whether the node is None
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            value =  l1val + l2val  + toadd
            toadd = int(value/10)
            value = value%10
            ans.next = ListNode(value)
            ans = ans.next

            # The node will stop at None
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if toadd == 1:
            ans.next = ListNode(1)
        startpoint = startpoint.next
        return startpoint

            

        

            