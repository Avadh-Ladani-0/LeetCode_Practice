class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        st=[]
        push="Push"
        pop="Pop"
        for i in range(1,n+1):
            if st==target:
                return ans
            if i not in target:
                ans.append(push)
                ans.append(pop)
            else:
                ans.append(push)
                st.append(i)
            

        return ans