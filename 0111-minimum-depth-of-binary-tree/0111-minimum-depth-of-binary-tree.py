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
        
        level = [float('inf')]
        def dfs (root, l):
            if not root:
                return
            if not root.left and not root.right:
                level[0] = min(level[0], l)
            
            l += 1
            
            dfs(root.left, l)
            dfs(root.right, l)
        
        dfs(root, 1)
        return level[0]