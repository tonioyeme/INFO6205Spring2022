#generate a dummy head
#add the nodes in two linkedlists
#go to next nodes
#use carry to count when sum > 10


class Solution(object):
    def addTwoNumbers(self, l1, l2):
		dummy = curr = ListNode(-1)

		carry = 0

		while l1 or l2 or carry:
			if l1:
				curr.val += l1.val
				l1 = l1.next

			if l2:
				curr.val += l2.val
				l2 = l2.next

			if carry:
				curr.val += carry
	
		carry = curr.val // 10
		curr.val %= 10
		curr = curr.next

		return dummy.next

