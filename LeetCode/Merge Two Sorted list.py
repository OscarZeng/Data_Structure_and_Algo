#Merge two sorted lists, linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            ans = ListNode(l1.val)
            l1 = l1.next
        else:
            ans = ListNode(l2.val)
            l2 = l2.next
        start = ans

        while (l1 or l2):
            if l1 == None:
                ans.next = l2
                break
            elif l2 == None:
                ans.next = l1
                break
            else:
                if l1.val <= l2.val:
                    ans.next = ListNode(l1.val)
                    l1 = l1.next
                    ans = ans.next
                else:
                    ans.next = ListNode(l2.val)
                    l2 = l2.next
                    ans = ans.next
        
        return start