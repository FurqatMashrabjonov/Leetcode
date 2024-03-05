# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lefts = []
        def dfs(root):
            if not root:
                return False
            dfs(root.left)
            
            lefts.append(root.val)
            
            dfs(root.right)
            
        dfs(root)
        
        return lefts[k - 1]