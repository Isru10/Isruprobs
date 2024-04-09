# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=collections.deque()
        q.append(root )
        res=[]
        while q :
            lvl=[]
            qlen=len(q)
            for i in range(qlen):
                node=q.popleft()
                if node:
                    
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl :
                res.append(lvl)
        return res