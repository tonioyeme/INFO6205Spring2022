class Solution:
    import collections
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index):
            pivot_freq = count[unique[pivot_index]]
            store_index = left
            unique[pivot_index], unique[right] =  unique[right], unique[pivot_index]
            
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[i], unique[store_index] = unique[store_index], unique[i]
                    store_index += 1
            
            unique[store_index], unique[right] = unique[right], unique[store_index]
            
            return store_index
        
        def selection(left, right, k_smallest):
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if left == right and k_smallest > 1:
                return
            if k_smallest < pivot_index:
                return selection(left, pivot_index-1, k_smallest)
            elif k_smallest > pivot_index:
                return selection(pivot_index+1, right, k_smallest)
            elif k_smallest == pivot_index:
                return
        
        selection(0, len(unique)-1, len(unique)-k)
        return unique[len(unique)-k:]