class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = Counter(nums)
        res  = sorted(nums, key = lambda x: (counts[x], -x))
        
        return res