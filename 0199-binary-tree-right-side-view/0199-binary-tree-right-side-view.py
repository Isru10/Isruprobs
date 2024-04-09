# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue =deque()
        queue.append(root)
        if not root :return []
        ans =[]
        while queue:
            notadded=True 
            maxlen=len(queue)
            for i in range(maxlen):
                node=queue.popleft()
                if node : 
                    if notadded:
                        ans.append(node.val)
                        notadded=False
                    queue.append(node.right)
                    queue.append(node.left)
        return ans 
        