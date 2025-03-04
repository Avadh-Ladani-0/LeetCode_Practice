class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power=[]
        while n>0:
            temp=0
            i=0
            while temp<=n:
                temp=3**i
                i+=1
            
            if i-2 in power:
                return False
            else:
                power.append(i-2)
                print(power)

            if 3**(i-2)==n or temp==n:
                return True

            n=n-3**(i-2)
            print(n)