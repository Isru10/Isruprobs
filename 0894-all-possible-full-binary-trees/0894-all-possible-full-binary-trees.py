# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp={0:[],1:[TreeNode()]}
        def back(n):
            if n in dp :
                return dp[n]
            res=[]
            for l in range(n):
                r=n-1-l
                left,right=back(l),back(r)
                for t1 in left:
                    for t2 in right:
                        res.append(TreeNode(0,t1,t2))
            dp[n]=res
            return res
        return back(n)