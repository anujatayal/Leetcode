
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
# without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Input: s = "abc", t = "ahbgdc"
# Output: true

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # print(s[:-1])
        if len(s)>0 and len(t)==0:
            return False
        elif len(s)==0:
            return True
        elif s[-1]==t[-1]:
            return self.isSubsequence(s[:-1], t[:-1])
        else:
            return self.isSubsequence(s, t[:-1])