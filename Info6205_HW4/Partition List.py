# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        beforeT = beforeH = ListNode(-1)
        afterT = afterH = ListNode(-1)
        
        while head:
            if head.val < x:
                beforeT.next = head
                beforeT = beforeT.next
            else:
                afterT.next = head
                afterT = afterT.next
            
            head = head.next
        
        afterT.next = None
        beforeT.next = afterH.next
        
        return beforeH.next
            
        