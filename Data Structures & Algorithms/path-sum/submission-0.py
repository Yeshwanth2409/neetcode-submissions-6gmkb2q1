# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, res):
            if not node:
                return False

            res += node.val

            if  not node.left and not node.right:
                return res == targetSum

            return dfs(node.left, res) or dfs(node.right,res)

        return dfs(root, 0)