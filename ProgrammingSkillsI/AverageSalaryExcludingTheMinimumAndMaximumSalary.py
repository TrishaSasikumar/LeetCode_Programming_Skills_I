def average(self, salary: List[int]) -> float:
    min=salary[0]
    max=salary[0]
    sum=0
    size=len(salary)
        # print(size)
    for i in range(size):
             
        if (salary[i]<min):
            min=salary[i]
        if(salary[i]>max):
            max=salary[i]
        sum+=salary[i]
            
    x=float("%.5f" %((sum-min-max)/(size-2)*1.00000))
    return x
