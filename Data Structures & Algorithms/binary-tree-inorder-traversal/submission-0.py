# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
    
        result = []

        left = root.left
        right = root.right

        if left:
            result.extend(self.inorderTraversal(left))
        
        result.append(root.val)

        if right:
            result.extend(self.inorderTraversal(right))
        
        return result