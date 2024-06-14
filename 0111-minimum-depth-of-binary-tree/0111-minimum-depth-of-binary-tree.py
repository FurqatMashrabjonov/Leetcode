# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = [float('inf')]
        
        def dfs(root, level):
            if not root:
                return
            if not root.left and not root.right:
                res[0] = min(res[0], level)
            
            level += 1
            
            dfs(root.left, level)
            dfs(root.right, level)
        
        dfs(root, 1)
        return res[0]
            
            