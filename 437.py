# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        # if only return DFS(root, sum), 
        return self.DFS(root, sum) + self.pathSum(root.left, sum) +self.pathSum(root.right, sum)
        
    def DFS(self, root, value):
        if root == None:
            return 0
        if root.val == value:
            return 1 + self.DFS(root.left, value - root.val)+ self.DFS(root.right, value - root.val)
        return self.DFS(root.left, value - root.val) + self.DFS(root.right, value - root.val)