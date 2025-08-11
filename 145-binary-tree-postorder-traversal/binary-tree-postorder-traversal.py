# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left_order = self.postorderTraversal(root.left)
        right_order = self.postorderTraversal(root.right)
        current = [root.val]
        return left_order + right_order + current