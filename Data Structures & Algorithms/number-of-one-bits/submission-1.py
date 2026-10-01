class Solution:
    def hammingWeight(self, n: int) -> int:
        if n <= 0:
            return 0
        if n%2!=0:
            return 1+self.hammingWeight(n//2)
        else:
            return self.hammingWeight(n//2)        
