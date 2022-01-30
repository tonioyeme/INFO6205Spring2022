class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        counter = Counter(s)
        pq = [(-value, key) for key, value in counter.items()]
        heapq.heapify(pq)
        log_count = 0
        log_char = ""
        
        while pq:
            count, char = heapq.heappop(pq)
            res += char
            
            if log_count < 0:
                heapq.heappush(pq, (log_count, log_char))
            
            count += 1
            log_count = count
            log_char = char
            
        if len(res) != len(s):
            return ""
        
        return res