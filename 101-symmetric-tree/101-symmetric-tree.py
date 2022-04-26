# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left and root.right:
            return self.is_symmetric(root.left,root.right)
        if root.left or root.right:
            return False
        return True
    
    
    def is_symmetric(self, left, right):

        if left is None and right is None:
            return True
        if right is None or left is None or left.val != right.val:
            return False
        return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left) 