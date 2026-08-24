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

                print('Temp:')
                for node in temp:
                    print(node.val)
                print('Res: {}'.format(res))
                print('Stack1:')
                for node in stack1:
                    print(node.val)

                if (not stack1) and temp:
                    stack1 = temp
                    print('Stack1 is now empty. New stack1:')
                    for node in stack1:
                        print(node.val)
                    res.append(temp[-1].val)
                    temp = []
                
                print('New iteration /n')
                
        
        return res
