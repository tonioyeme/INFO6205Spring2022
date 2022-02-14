class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0,head)
        pred = dummyhead
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            
            head = head.next
        return dummyhead.next