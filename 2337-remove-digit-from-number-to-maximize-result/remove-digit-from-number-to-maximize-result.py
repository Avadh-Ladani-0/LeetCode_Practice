class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxi=0
        for i in range(len(number)):
            if number[i]==digit:
                temp=int(number[:i]+number[i+1:])
                maxi=max(maxi,temp)
        return str(maxi)