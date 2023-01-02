class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pos=0;
        neg=0;
        for i in nums:
            if i==0:
                return 0;
            elif i>0:
                pos+=1;
            else:
                neg+=1;
        if neg%2==1:
            return -1;
        else:
            return 1;