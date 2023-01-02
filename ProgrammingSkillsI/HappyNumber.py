class Solution:
    def isHappy(self, n: int) -> bool:
        
        s=set();
        s.add(n);
        while(True):
            sum=0;
            while n!=0:
                m=n%10
                sum+=(m*m);
                n=n//10;
            # print(sum);
            if sum==1:
                return True; 
            n=sum;          
            if n in s:
                return False;
            s.add(sum) ;