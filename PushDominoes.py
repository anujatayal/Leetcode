# There are n dominoes in a line, and we place each domino vertically upright. 
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. S
# imilarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already 
# fallen domino.
# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

#Approach- force decreases as we move far away from original force.
#finally if value>0, it will push towards R, if value<0, it will push towards left else remain in same state
#22nd July 2021
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        force=[]
        n=len(dominoes)
        value=0
        for i in dominoes:
            if i=='R':
                value=n
            elif i=='L':
                value=0
            else:
                value=max(value-1,0)
            force.append(value)      
        for i in range(len(dominoes)-1,-1,-1):
            if dominoes[i]=='L':
                value=n
            elif dominoes[i]=='R':
                value=0
            else:
                value=max(value-1,0)
            force[i]-=value     
        result=''
        for i in force:
            if i<0:
                result+='L'
            elif i>0:
                result+='R'
            else:
                result+='.'
        return(result)