class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)
        
        heap = (heapq.nsmallest(k, counts.items(), key = lambda x: (-x[1], x[0])))
        
        return [word for word, count in heap]