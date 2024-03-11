# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, minVal, maxVal):
            if root == None:
                return True
            
            if minVal < root.val < maxVal:
                return check(root.left, minVal, root.val) and check(root.right, root.val, maxVal)
            else:
                return False
        
        
        return check(root, -1 * 2**31 - 1, 2**31) 