# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting
#  some or no elements without changing the order of the remaining elements.
# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#9th nov
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        mat=[[0 for i in range(len(s))] for j in range(len(s))]
        len1=0
        while(len1!=len(s)):
            for i in range(len(s)-len1):
                if len1==0:
                    mat[i][i+len1]=1
                elif s[i]==s[i+len1]:
                    mat[i][i+len1]=2+mat[i+1][i+len1-1]
                else:
                    mat[i][i+len1]=max(mat[i+1][i+len1],mat[i][i+len1-1])
            len1+=1
        return mat[0][len(s)-1]