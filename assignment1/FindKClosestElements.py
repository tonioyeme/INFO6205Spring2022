class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort( key = lambda num: abs(x-num))
        print(arr)
        res = []
        for i in range(k):
            res.append(arr[i])
        
        return sorted(res)