class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        ops=["+","-","*","/"]

        for ele in tokens:
            if ele not in ops:
                st.append(int(ele))
            else:
                n2=st.pop()
                n1=st.pop()
                if ele=="+":
                    st.append(n1+n2)
                elif ele=="-":
                    st.append(n1-n2)
                elif ele=="*":
                    st.append(n1*n2)
                else:
                    st.append(math.trunc(n1/n2))
        
        return st[0]
