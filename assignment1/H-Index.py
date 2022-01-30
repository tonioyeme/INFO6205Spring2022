class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while i in range(len(citations)) and citations[i] >= i + 1:
            i += 1
        
        return i