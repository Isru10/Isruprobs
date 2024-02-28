# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=[root]
        leftMost=root.val
        while len(queue):
            nextqueue=[]
            while len(queue):
                curr=queue.pop(0)
                if curr.left :
                    nextqueue.append(curr.left)
                if curr.right :
                    nextqueue.append(curr.right)
            queue=nextqueue
            leftMost=nextqueue[0].val if len(nextqueue) else leftMost
        return leftMost