######LRUCache, typical code for object/structure implementation########
########################################################################
class DlinkNode:
    #properly define the data structure with double linked list plus dictionary
    def __init__(self, key= None, value = None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.Cache = {}
        self.dummyhead = DlinkNode()
        self.dummytail = DlinkNode()
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead
        self.capacity = capacity
        self.size = 0

    def removeNode(self, theNode):
        theNode.prev.next = theNode.next
        theNode.next.prev = theNode.prev

    def addToLatest(self, theNode):
        theNode.next = self.dummytail
        theNode.prev = self.dummytail.prev
        self.dummytail.prev.next = theNode
        self.dummytail.prev = theNode

    def moveToLatest(self, theNode):
        self.removeNode(theNode)
        self.addToLatest(theNode)

    def deleteOldest(self):
        oldestNode = self.dummyhead.next
        self.removeNode(oldestNode)
        return oldestNode

    def get(self, key: int) -> int:
        if key not in self.Cache:
            return -1
        else:
            theNode = self.Cache[key]
            self.moveToLatest(theNode)
            return theNode.value


    def put(self, key: int, value: int) -> None:
        if (key not in self.Cache):
            newNode = DlinkNode(key, value)
            self.Cache[key] = newNode
            self.addToLatest(newNode)
            self.size += 1
            if self.size > self.capacity:
                oldestNode = self.deleteOldest()
                self.Cache.pop(oldestNode.key)
                self.size -= 1
        else:
            theNode = self.Cache[key]
            theNode.value = value
            self.moveToLatest(theNode)
        

        return None
            

############Inner Function that use inner function mutable objects#########################
###########################################################################################
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def GPDFS (left, right, S):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append('(')
                #Here the S is immutable object, passing to another function will make a copy
                GPDFS(left+1, right, S)
                S.pop()
            if right < left:
                S.append(')')
                GPDFS(left, right+1, S)
                S.pop()
        
        GPDFS(0,0,[])
        return ans



#############The Usage of recurrsion as a parameter inside the function####################
###########################################################################################
def permute(self, nums):
    if len(nums) == 1:
        return [nums]
    ans = []
    #Here we use the recursion. 
    #Attach each element to the permmute of the rest of the element
    for i in nums:
        currentNums = nums.copy()
        currentNums.remove(i)
        #Recursion doesn't have to be at the end
        #Here we consider the permute function as a generator of previous pattern
        permuteNums = self.permute(currentNums)
        for j in permuteNums:
            ans.append([i]+j)
    return ans


#############Binary tree use the recurrsion that check left tree and right tree############
###########################################################################################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        iniMax = float('inf')
        iniMin = float('-inf')
        #When it comes to check something, usually we will use the recursion due to the structure of Binary Tree
        #Here the key point is that for any BST, the root value shall be bigger than all the value in the left and all the value in the right 
        def helper (root, Max, Min):
            #The null tree is true
            if root == None:
                return True
            if root.val >= Max or root.val <= Min:
                return False
            isLeftBST = helper(root.left, root.val, Min)
            isRightBST = helper(root.right, Max ,root.val)
            return isLeftBST and isRightBST
        
        return helper(root, iniMax, iniMin)

#############For 2D matrix implement DFS count num of islands#############################
##########################################################################################
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m,n = len(grid), len(grid[0])
        checked = [[False]*n for _ in range(m)]
        #print(grid)
        ans = 0

        def DFS(i,j):
            stack = [(i,j)]
            while len(stack) != 0:
                Index = stack.pop()
                currI, currJ =  Index[0], Index[1]
                if checked[currI][currJ] == True:
                    continue
                else:
                    checked[currI][currJ] = True
                #Check the surrounding pixes
                if currI != 0:
                    if grid[currI-1][currJ] == "1":
                        stack.append((currI-1, currJ))
                if currI != m-1:
                    if grid[currI+1][currJ] == "1":
                        stack.append((currI+1, currJ))
                if currJ != 0:
                    if grid[currI][currJ-1] == "1":
                        stack.append((currI, currJ-1))
                if currJ != n-1:
                    if grid[currI][currJ+1] == "1":
                        stack.append((currI, currJ+1))

        for i in range (m):
            for j in range(n):
                if checked[i][j] == True or grid[i][j] == "0":
                    continue
                else:
                    DFS(i, j)
                    #print(checked)
                    ans += 1

        return ans

###############Linked list implementation#################################################
##########################################################################################
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 0
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
        #Create a new linked list
        while mNode != head:
            mNode = mNode.next
            newNode = ListNode(mNode.val)
            newNode.next = front
            front = newNode
        begin.next = front 
        back.next = end

        return dummy.next


#####################Binary search implementation#########################################
##########################################################################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        #The checking range is [left, right] both sides included
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # left part is in order
            if nums[mid] >= nums[left]:
                #Since mid is already checked, we don't include them
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right part is in order
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



#########################Dynamic programming implementation################################
###########################################################################################
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        Upaths = [[0]*m for _ in range(n)]
        Upaths[0][0] = 1
        for i in range(n):
            for j in range(m):
                if (i == 0) and (j ==0):
                    continue
                if i == 0:
                    Upaths[i][j] = Upaths[i][j-1]
                elif j == 0:
                    Upaths[i][j] = Upaths[i-1][j]
                else:
                    Upaths[i][j] = Upaths[i-1][j] + Upaths[i][j-1]
        return Upaths[n-1][m-1]