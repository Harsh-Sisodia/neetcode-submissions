class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        Hash = [0]*26

        for i in range(len(t)):
            Hash[ord(s[i])-97]+=1
            Hash[ord(t[i])-97]-=1

        for val in Hash:
            if val!=0:
                return False
        else:
            return True