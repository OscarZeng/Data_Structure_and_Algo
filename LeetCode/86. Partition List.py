# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #Here we use two linked list to store those nodes in front and in the back
        small, big = ListNode('s'), ListNode('b')
        startSmall = small
        startBig = big
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        #Here we need to end the list!!!
        big.next = None
        #Connect the big list to the small list
        small.next = startBig.next
        #remember to eliminate the first dummy node
        return startSmall.next