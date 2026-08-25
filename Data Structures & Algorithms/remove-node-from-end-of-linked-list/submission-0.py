# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # count total nodes (sz)
        # if n == sz, remove head, new head = head.next
        # if n < sz, remove (sz - n)th node -> sz=4, n=2, rm 2nd node (start=0=head)
        sz = 0
        curr = head

        while (curr != None):
            sz = sz + 1
            curr = curr.next
        
        if (n == sz):
            head = head.next
        
        if (n < sz):
            count = 0
            curr = head
            while count < (sz - n - 1): # c < 1
                curr = curr.next
                count = count + 1
            
            curr.next = curr.next.next
        
        return head


