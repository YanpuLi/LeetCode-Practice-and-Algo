# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.acc(root, 0) 
    def acc(self,root, flag):
        if root == None:
            return 0
        if root.left == None and root.right == None and flag:
            return root.val
        return self.acc(root.left, 1) + self.acc(root.right, 0)
    