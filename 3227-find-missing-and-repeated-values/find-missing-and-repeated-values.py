class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq=[0]*((len(grid)*len(grid[0]))+1)
        freq[0]=1
        dup=int()
        missing=int()
        for i in grid:
            for j in i:
                freq[j]+=1

        for i in range(1,len(freq)):
            if freq[i]==2:
                dup=i
            if freq[i]==0:
                missing=i

        return [dup,missing]
        

