# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 0
        #Here we create the dummy node in the front in case it reverse from the very beginning
        dummy = ListNode('a')
        dummy.next = head
        head = dummy
        while count < n:
            if count == m-1:
                begin = head
                mNode = head.next
            head = head.next
            count += 1
        end = head.next
        #print(begin.val, mNode.val ,head.val, end.val)
        front = ListNode(mNode.val)
        back = front
        #Create a new linked list and replace the new linked list with that
        while mNode != head:
            mNode = mNode.next
            newNode = ListNode(mNode.val)
            newNode.next = front
            front = newNode
        begin.next = front 
        back.next = end

        return dummy.next
            