class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        peri=0
        lar=0;
        size=len(nums);
        nums.sort();
        print(nums);

        for i in range(size-2):
            a=nums[i];b=nums[i+1];c=nums[i+2];
            if (a+b>c) and (b+c>a)and (a+c>b):
                peri=a+b+c;
                if(peri>lar) : lar=peri; 
        return lar; 