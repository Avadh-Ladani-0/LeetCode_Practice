class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power=[]
        while n>0:
            i=0
            while 3**i<=n:
                i+=1

            if i-1 in power:
                return False
            else:
                if 3**(i-1)==n:
                    return True
                else:
                    power.append(i-1)
                    print(power)

            n=n-3**(i-1)
            print(n)