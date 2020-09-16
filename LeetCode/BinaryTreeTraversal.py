# Binary Tree Traversal, Preorder, inorder, postorder
#Recursive:
def PreOrder(self, root):
		'''打印二叉树(先序)'''
		if root == None:
			return 
		print(root.val, end=' ')
		self.PreOrder(root.left)
		self.PreOrder(root.right)

def InOrder(self, root):
		'''中序打印'''
		if root == None:
			return
		self.InOrder(root.left)
		print(root.val, end=' ')
		self.InOrder(root.right)

def BacOrder(self, root):
		'''后序打印'''
		if root == None:
			return
		self.BacOrder(root.left)
		self.BacOrder(root.right)
		print(root.val, end=' ')
#Non_Recursive

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
 
class Solution(object):
    #二叉树非递归前序序遍历
    def pre_order(self, root):
        if not root:
            return None
        node_list = []
        p = root
        res = []
        while p or len(node_list):
            # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
            while p:
                node_list.append(p)
                res.append(p.val)
                p = p.left
            # 开始出栈
            if len(node_list):
                p = node_list[-1]
                node_list.pop()
                p = p.right
        return res
 
    # 二叉树非递归中序遍历
    def middle_order(self, root):
        node_list = []
        p = root
        res = []
        while p or len(node_list) != 0:
            # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
            while p:
                node_list.append(p)
                p = p.left
            # 开始出栈
            if len(node_list):
                p = node_list[-1]
                node_list.pop()
                res.append(p.val)
                # 进入右子树
                p = p.right
        return res
 
    #二叉树非递归后序序遍历
    def post_order(self, root):
        if not root:
            return None
        node_list = []
        p = root
        pLast = None
        res = []
        # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
        while p:
            node_list.append(p)
            p = p.left
        # 开始出栈
        while len(node_list):
            p = node_list[-1]
            node_list.pop()
            # 若无右子树或者右子树被访问，则访问该节点
            if not p.right or p.right == pLast:
                res.append(p.val)
                pLast = p
            else:
                # 节点再次入栈
                node_list.append(p)
                p = p.right
                while p:
                    node_list.append(p)
                    p = p.left
        return res
 
 
 
def main():
    solution = Solution()
    root = TreeNode(8)
    root.left = TreeNode(6)
    node1 = root.left
    root.right = TreeNode(10)
    node2 = root.right
    node1.left = TreeNode(5)
    node1.right = TreeNode(7)
    node2.left = TreeNode(9)
    node2.right = TreeNode(11)
    print(solution.post_order(root))
 
 
if __name__ == '__main__':
    sys.exit(main())
