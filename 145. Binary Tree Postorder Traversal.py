# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        t=[]
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            
            inOrder(root.right)
            t.append(root.val)
        inOrder(root)
        return t