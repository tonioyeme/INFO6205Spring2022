class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count1, count2, candidate1, candidate2 = 0,0,None,None
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
            
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)/3:
                res.append(c)
        
        return res