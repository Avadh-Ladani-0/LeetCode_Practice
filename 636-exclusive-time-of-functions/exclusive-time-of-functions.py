class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def process(s):
            i=0
            while s[i]!=":":
                i+=1
            id=int(s[:i])
            state=0 if s[i+1]=="s" else 1
            
            i=len(s)-1
            while s[i]!=":":
                i-=1
            ts=int(s[i+1:])

            return (id,state,ts)
        
        ans=[0]*n
        stack=[]
        prev_ts=0

        for i in logs:
            id,state,ts=process(i)
            
            if state==0:
                if len(stack)!=0:
                    ans[stack[-1]]+=ts-prev_ts
                stack.append(id)
                prev_ts=ts
            
            else:
                ans[stack.pop()]+=ts-prev_ts+1
                prev_ts=ts+1
            
        return ans

            