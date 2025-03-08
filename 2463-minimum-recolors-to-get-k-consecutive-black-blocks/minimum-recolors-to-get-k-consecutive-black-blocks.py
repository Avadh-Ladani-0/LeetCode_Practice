class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mini=float('+inf')
        for i in range(len(blocks)-(k-1)):
            t_count=0
            for j in range(i,i+k):
                print(blocks[j],end="")
                if blocks[j]=='W':
                    t_count+=1
                
            mini=min(t_count,mini)
            print(mini,t_count)
        
        return mini