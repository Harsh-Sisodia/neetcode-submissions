class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxi = 0
        start = 0
        mdict = dict()

        for i in range(0,len(s)):
            if s[i] in mdict and mdict[s[i]]>=start:
                start = mdict[s[i]]+1
            mdict[s[i]]=i
            maxi = max(maxi,i-start+1)
        return maxi 


            
            



            