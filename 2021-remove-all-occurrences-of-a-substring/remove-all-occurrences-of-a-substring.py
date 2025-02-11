class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st_string=""
        if len(part)>len(s):
            return s
        for i in range(len(part)-1):
            st_string+=s[i]

        for i in range(len(part)-1,len(s)):
            st_string+=s[i]
            if st_string[len(st_string)-len(part):len(st_string)]==part:
                st_string=st_string[:len(st_string)-len(part)]
        
        return st_string
                



            