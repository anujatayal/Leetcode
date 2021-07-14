# order and str are strings composed of lowercase letters. In order, no letter occurs more than once.
# order was sorted in some custom order previously. We want to permute the characters of str so that they match the order 
# that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.
# Return any permutation of str (as a string) that satisfies this property.

# Input: 
# order = "cba"
# str = "abcd"
# Output: "cbad"
#14th July 2021
#Approach- Store index of ord in strDict and store their count in count.
#sort strDict acc to value and print based on count
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        strDict={}   
        count={}
        for char in str:
            if char in strDict:
                count[char]=count[char]+1
            elif char in order:
                strDict[char]=order.index(char)
                count[char]=1
            else:
                strDict[char]=27
                count[char]=1
        sortList=sorted(strDict.items(), key =lambda kv:kv[1])
        req=[items[0] for items in sortList]
        finalStr=''
        for i in req:
            finalStr+=i*count[i]
        return(finalStr)
            