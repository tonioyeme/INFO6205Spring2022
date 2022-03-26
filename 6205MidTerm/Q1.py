#traverse elements in array nums, if any elements in the range: continue to next one, if not: append it in the answer array

class Solution(object):
    def getMissings(self, nums, lower, upper):

		ans = []
		res = []

		for num in nums:
			if lower <= num <= upper:
			continue
			res.append(num)

		ans.append(res[0])
		ans.append(res[-1])

		return ans
