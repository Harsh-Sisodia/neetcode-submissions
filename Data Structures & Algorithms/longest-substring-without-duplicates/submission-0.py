class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        

        for i in range(0,len(s)):
            mset = set()
            for j in range(i,len(s)):
                if s[j] in mset:
                    break;
                mset.add(s[j])
                maxi = max(maxi,j-i+1) 
        return maxi

            
            



            