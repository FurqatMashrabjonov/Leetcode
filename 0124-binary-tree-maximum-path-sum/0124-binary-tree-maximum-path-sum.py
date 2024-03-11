# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -1000
        
        def find(root):
            if not root:
                return 0
            
            left = find(root.left)
            right = find(root.right)
            
            leftMax = max(0, left)
            rightMax = max(0, right)
            
            self.maxPath = max(
                self.maxPath,
                root.val + leftMax + rightMax,
            )
            
            return root.val + max(leftMax, rightMax)
        find(root)
        return self.maxPath