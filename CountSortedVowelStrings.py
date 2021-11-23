# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) 
# and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes 
# before s[i+1] in the alphabet.
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

# 28th Oct 2021
# Using math and dp

class Solution:
    def countVowelStrings(self, n: int) -> int:
        nos=[1,1,1,1,1]
        for i in range(n-1):
            for j in range(len(nos)):
                nos[j]=sum(nos[j:])
        return sum(nos)
                