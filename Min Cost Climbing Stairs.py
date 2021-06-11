# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
#complexity
#space O(n)
#time O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost=[]
        for i in range(len(cost)):
            if i==0:
                minCost.append(cost[i])
            elif i==1:
                minCost.append(cost[i])
            else:
                minCost.append(cost[i]+min(minCost[i-1],minCost[i-2]))
            # print(i,minCost)
        return min(minCost[i],minCost[i-1])