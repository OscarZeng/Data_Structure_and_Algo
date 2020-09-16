"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        copyNodeDict = {}
        #The starting point of the copy list
        copyHead = Node(head.val)
        copyPointer = copyHead
        pointer = head
        copyNodeDict[head] = copyHead
        while pointer != None:
            pointer = pointer.next
            if pointer != None:
                copyPointer.next = Node(pointer.val)
            else:
                copyPointer.next = None
            copyPointer = copyPointer.next
            
            #print(copyNodeDict)
            if pointer !=None:
                copyNodeDict[pointer] = copyPointer
                #print(pointer.val, copyPointer.val)
        pointer = head
        copyPointer = copyHead
        while pointer != None:
            if pointer.random == None:
                copyPointer.random = None
            else:
                copyPointer.random = copyNodeDict[pointer.random]
            #if copyPointer.random != None:
                #print(copyPointer.random.val)
            pointer = pointer.next
            copyPointer = copyPointer.next

        return copyHead 
            

