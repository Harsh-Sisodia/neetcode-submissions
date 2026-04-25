class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-97]+=1
            key = tuple(count)
            if key in res:
                res[key].append(i)
            else:
                res[key]=[i]
        return list(res.values())

