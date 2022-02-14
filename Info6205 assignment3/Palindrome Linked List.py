class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val = []
        curr = head
        while curr:
            val.append(curr.val)
            curr = curr.next
        return val[::-1] == val