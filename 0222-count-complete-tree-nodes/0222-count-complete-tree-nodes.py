# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not  root :return 0
        def ll(node):
            if not node :return 0
            return 1+ll(node.left)
        def rr(node):
            if not node :return 0
            return 1+rr(node.right)
        l=ll(root)
        r=rr(root)
        if l > r:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
            
            
        else:
            return (2**l)-1
        
        