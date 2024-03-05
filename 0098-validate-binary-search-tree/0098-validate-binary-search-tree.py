# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minval, maxval = -1 * 2**31 - 1, 2**31
        
        return self.isValid(root, minval, maxval)
        
    def isValid(self, root, minval, maxval):
        if not root:
            return True
        elif minval < root.val < maxval:
            return self.isValid(root.left, minval, root.val) and self.isValid(root.right, root.val, maxval)
        else:
            return False