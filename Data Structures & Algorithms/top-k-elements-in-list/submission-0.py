class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map  = {}

        for i in nums:
            hash_map[i]= 1 + hash_map.get(i,0)
        
        res = []

        for i in range(k):
            e = max(hash_map,key=hash_map.get)
            res.append(e)
            hash_map.pop(e)

        return res

