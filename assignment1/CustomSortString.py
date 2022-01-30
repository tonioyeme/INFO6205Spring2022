import collections
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        res =  []
        
        for char in order:
            res.append(char*count[char])
            count[char] = 0
        
        for char in count.keys():
            print(char)
            res.append(char*count[char])
            
        return "".join(res)