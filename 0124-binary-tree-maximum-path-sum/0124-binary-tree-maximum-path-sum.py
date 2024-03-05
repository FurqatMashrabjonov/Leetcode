# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSum(root):
            if not root:
                return 0
            
            leftSum = maxSum(root.left)
            rightSum = maxSum(root.right)
            l = max(0, leftSum)
            r = max(0, rightSum)
            maxPath[0] = max(maxPath[0], l + r + root.val)
            
            return root.val + max(l, r)
        
        maxPath = [float('-inf')]
        maxSum(root)
        return maxPath[0]