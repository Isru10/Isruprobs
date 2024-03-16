# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p=root.left
        q=root.right
        a=[True]
        def sym(p,q,a):
            if p  is None and   q  is None:
                return 
            if  p   is None or  q   is None or p.val!=q.val:
                a[0]=False
                return
            sym(p.left,q.right,a)
            sym(p.right,q.left,a)
        sym(p,q,a)
        return a[0]
        