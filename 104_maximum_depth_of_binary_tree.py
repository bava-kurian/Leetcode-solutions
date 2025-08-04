# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ if not root:
            return 0
        left_sub=self.maxDepth(root.left)
        right_sub=self.maxDepth(root.right)
        return 1+max(left_sub,right_sub)"""
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            depth += 1
        
        return depth

        