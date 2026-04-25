class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxi = 0
        left = 0
        right = 0
        hash_dict = {}

        while right<len(s):
            
            if s[right] in hash_dict and hash_dict[s[right]]>=left:
                left = hash_dict[s[right]]+1
            
            maxi = max(maxi , right-left+1)
            hash_dict[s[right]]=right

            right+=1 
        return maxi

            
            



            