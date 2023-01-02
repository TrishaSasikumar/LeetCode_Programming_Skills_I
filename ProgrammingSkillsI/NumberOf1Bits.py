class Solution:
    def hammingWeight(self, n: int) -> int:
        m=str(bin(n));
        count=0;
        for i in m:
            if(i=="1"):
                count+=1;
        return count;