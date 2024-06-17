# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        res = []
        
        def helper(root, path):
            if not root:
                return
            path += '->' + str(root.val)
            if not root.left and not root.right:
                res.append(path[2:])
                return
            
            helper(root.left, path)
            helper(root.right, path)
            
        
        
        helper(root, '')
        
        return res