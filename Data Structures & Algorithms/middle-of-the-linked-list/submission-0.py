# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # [1,2,3,4,5] -> (2,3), (3,5)
        # [1,2,3,4,5,6] -> (2,3), (3,5), (4,6)

        if head == None:
            return
        
        slow, fast = head, head
        
        while fast.next: # (2,3), (3,5), (4,6)
            slow = slow.next
            
            fast = fast.next
            if fast.next:
                fast = fast.next
        
        return slow