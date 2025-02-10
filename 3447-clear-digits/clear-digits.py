class Solution:
    def clearDigits(self, s: str) -> str:
        ans=""
        index=[]
        for i in range(len(s)):
            if s[i].isdigit():
                for j in range(i-1,-1,-1):
                    if s[j].isdigit()==False:
                        if j not in index:
                            index.append(j)
                            break
        
        for i in range(len(s)):
            if s[i].isdigit() == False and  i not in index:
                ans+=s[i]

        return ans