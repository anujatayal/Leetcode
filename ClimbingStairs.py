
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# Naive Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<0:
            return 0
        elif n==1 or n==0:
            return 1
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
            
# Memoization    
class Solution:
    def memoization(self,memo,n:int)->int:
        if n in memo:
            return memo[n]
        elif n<0:
            return 0
        elif n==1 or n==0:
            return 1
        else:
            memo[n]=self.memoization(memo,n-1)+self.memoization(memo,n-2)
            return memo[n]
    def climbStairs(self, n: int) -> int:
        memo={}
        if n<0:
            return 0
        elif n==1 or n==0:
            return 1
        else:
            return self.memoization(memo,n)