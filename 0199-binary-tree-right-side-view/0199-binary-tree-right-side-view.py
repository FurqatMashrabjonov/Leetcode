# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not root:
            return res
        
        queue = [root]
        
        while len(queue):
            n = len(queue)
            res.append(queue[-1].val)
            for i in range(n):
                cur = queue.pop(0)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
         
        return res