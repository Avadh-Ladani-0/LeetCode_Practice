class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # brute force

        # mini=float('+inf')
        # for i in range(len(blocks)-(k-1)):
        #     t_count=0
        #     for j in range(i,i+k):
        #         print(blocks[j],end="")
        #         if blocks[j]=='W':
        #             t_count+=1
                
        #     mini=min(t_count,mini)
        #     print(mini,t_count)

        # optimal
        
        mini=0

        for i in range(k):
            if blocks[i]=='W':
                mini+=1
        
        t_c=mini

        for i in range(k,len(blocks)):
            if blocks[i]=='W':
                t_c+=1
            if blocks[i-k]=='W':
                t_c-=1
            mini=min(mini,t_c)

        return mini
        
        return mini