class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        
        
        if len(set1) < len(set2):
            return self.setIntersection(set1,set2)
        else:
            return self.setIntersection(set2,set1)
            
            
    def setIntersection(self, set1, set2):
        return [x for x in set1 if x in set2]