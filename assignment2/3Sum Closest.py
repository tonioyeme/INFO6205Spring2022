class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float("inf")
        nums.sort()
        
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums)-1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target-sum) < abs(diff):
                    diff = target - sum
                elif sum < target:
                    lo += 1
                else:
                    hi -= 1
        
        return target - diff