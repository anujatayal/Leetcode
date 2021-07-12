# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's 
# in the binary representation of i.
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

#Using Recursion
class Solution:
    def noBits(self,n:int)->int:
        if n==1:
            return 1
        return self.noBits(n//2)+n%2
    def countBits(self, n: int) -> List[int]:
        ans=[]
        ans.append(0)
        if n>=1:
            ans.append(1)
        for i in range(2,n+1):
            bits=self.noBits(i)
            ans.append(bits)
        return(ans)

#Using Dynamic Programming
