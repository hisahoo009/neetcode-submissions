# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        #3,8
        #3:[5,3]
        #8:[5,8]

        #3,4
        #3:[5,3]
        #4:[5,3,4]

        #2,4
        #2:[5,3,1,2]
        #4:[5,3,4]
        #2 set 4: [5,3]

        if root is None:
            return None

        # If both p and q are smaller than root, 
        # go to left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If both p and q are greater than root, 
        # go to right subtree
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If nodes n1 and n2 are on the opposite sides, 
        # root is the LCA
        return root
