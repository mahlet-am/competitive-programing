class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        z=0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i]>strs[j+1][i]:
                    z+=1
                    break
        return z   