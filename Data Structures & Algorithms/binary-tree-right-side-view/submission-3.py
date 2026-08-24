# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []

        if root != None:
            res = [root.val]  
            stack1, temp = [root], []

            while stack1:
                curr = stack1.pop(0)
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
                
                # temp=[2,3], res=[1,3]
                # temp=[4, 5], res=[1,3,5]
                # temp=[]

                # temp=[3,2], res=[1,3]
                # temp=[4], res=[1,3,4]
                # temp=[5], res=[1,3,4,5]

                if (not stack1) and temp:
                    stack1 = temp
                    res.append(temp[-1].val)
                    temp = []
                
        
        return res
