# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Input: s = "egg", t = "add"
# Output: true
# Input: s = "foo", t = "bar"
# Output: false
# Input: s = "bacd", t = "baba"
# Output: false
#Approach- Store mapping in dict
# 12th July 2021
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap={}
        for i in range(len(s)):
            if s[i] in charMap.keys():
                if charMap[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in charMap.values():
                    return False
                charMap[s[i]]=t[i]
        return True