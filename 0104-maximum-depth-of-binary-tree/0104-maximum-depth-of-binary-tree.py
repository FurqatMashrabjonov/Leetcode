# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs
        
        if not root:
            return 0
        level = 0
        queue = deque()
        queue.append(root)
        
        while len(queue):
            level += 1
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
        
        return level