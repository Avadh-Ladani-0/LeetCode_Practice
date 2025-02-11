class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st=[]
        if len(part)>len(s):
            return s
        for i in range(len(part)-1):
            st.append(s[i])

        for i in range(len(part)-1,len(s)):
            st.append(s[i])
            sts="".join(st)
            if sts[len(sts)-len(part):len(sts)]==part:
                st=st[:len(st)-len(part)]
        
        return "".join(st)
                



            