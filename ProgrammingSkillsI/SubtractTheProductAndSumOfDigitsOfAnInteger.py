class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1;
        summ=0;
        dig=0
        while n>0:            
                dig=n%10;
                summ+=dig;
                prod*=dig;
                n=n//10;
            
        return prod-summ