# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        ans = [[]]
        #Here we use the BFS
        queue = [(root, 1)]
        #Due to the tree, we don't need to record the seen since it will not go back
        while len(queue) != 0:
            current = queue.pop(0)
            if current[0] == None:
                continue
            #Still need to record the ans
            if current[1] > len(ans):
                ans.append([])
            #The logic is very similar to the preorder
            ans[current[1]-1].append(current[0].val)
            if current[0].left != None:
                queue.append((current[0].left, current[1]+1))
            if current[0].right != None:
                queue.append((current[0].right, current[1]+1))
        for i in range(len(ans)):
            if (i+1)%2 == 0:
                ans[i] = ans[i][::-1]
        return ans