#sort the array intervals  according to intervals[i][0]
#if intervals[i][1] >= intervals[i+1][0]: update intervals[i][1] -> intervals[i+1][1]
#if intervals[i][1] < intervals[i+1][0]: append intervals[i] into res

class Solution(object):
    def addTwoNumbers(self, intervals):
		ans = []

		intervals.sort(key = lambda x:x[0])
    	ans = [intervals[0]]
        
    
    	for interval in intervals:
        
       		if ans[-1][1] < interval[0]:
            	ans.append(interval)
        	else:
            	ans[-1][1] = max(interval[1], ans[-1][1])
		return ans