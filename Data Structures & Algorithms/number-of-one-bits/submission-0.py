class Solution:
    def hammingWeight(self, n: int) -> int:
        one = 0
        while n>0:
            if n%2!=0:
                one +=1
            n=n//2
        return one
        
