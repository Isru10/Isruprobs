# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        g=[0]
        m=0
        def dfs(root, m):
            if not root :return []
            if root.val>=m:
                g[0]+=1
            m=max(m, root.val)
            dfs(root.left,m)
            dfs(root.right,m)
        dfs(root,float("-inf"))
        return g[0]
   