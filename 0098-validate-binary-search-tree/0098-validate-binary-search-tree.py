# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN, MAX = -float('inf'), float('inf')
        
        def validate(root, minv, maxv):
            if not root:
                return True
            
            if minv < root.val < maxv:
                return validate(root.left, minv, root.val) and validate(root.right, root.val, maxv)
            else:
                return False
        
        return validate(root, MIN, MAX)