# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def same(root, minval, maxval):
            if not root:
                return True
            
            if root.val > minval and root.val < maxval:
                return same(root.left, minval, root.val) and same(root.right, root.val, maxval)
            else: return False
        
        return same(root, -float('inf'), float('inf'))