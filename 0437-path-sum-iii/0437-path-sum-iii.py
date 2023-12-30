# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count=0
        self.prefixsum={0:1}
        self.dfs(root,targetSum, 0)
        return self.count 
    def dfs(self, node :TreeNode , targetSum: int , cursum: int) -> None:
        if not node :
            return 
        cursum+=node.val
        self.count+=self.prefixsum.get(cursum-targetSum,0)
        self.prefixsum[cursum]=self.prefixsum.get(cursum,0)+1
        self.dfs (node.left, targetSum, cursum)
        self.dfs (node.right, targetSum, cursum)
        self.prefixsum[cursum]-=1