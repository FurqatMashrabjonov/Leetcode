# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def bfs(root):
            if root == None:
                return
            
            queue = [root]
            
            while len(queue) > 0:
                tmp = []
                for i in range(len(queue)):
                    cur = queue.pop(0)
                    tmp.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                res.append(tmp)
                
        bfs(root)
        return res