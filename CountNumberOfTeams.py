# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) 
# where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1)

#time limit exceeded n3
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        for i in range(len(rating)):
            for j in range(i,len(rating)):
                if rating[i]<rating[j]:
                    for k in range(j,len(rating)):
                        if rating[j]<rating[k]:
                            count+=1
                if rating[i]>rating[j]:
                    for k in range(j,len(rating)):
                        if rating[j]>rating[k]:
                            count+=1
        return count

#efficient soln n2
#idea take left and right soln and merge

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        for i in range(len(rating)):
            leftLess=0
            rightmore=0

            leftmore=0
            rightLess=0
            
            for j in range(i):
                if rating[j]<rating[i]:
                    leftLess+=1
                else:
                    leftmore+=1
            for j in range(i+1,len(rating)):
                if rating[j]>rating[i]:
                    rightmore+=1
                else:
                    rightLess+=1
            count+=(leftLess*rightmore)+(leftmore*rightLess)
        return count