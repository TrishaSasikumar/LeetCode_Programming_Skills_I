class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid=[]
        dist1=[]
        dist=[]
        for i in range(len(points)):
            x1=points[i][0] ; y1=points[i][1]
            if x1==x or y1==y:
                valid.append([x1,y1]);                
                dist.append(abs(x-x1)+abs(y-y1));
                dist1.append(abs(x-x1)+abs(y-y1));               
            else:
                valid.append(["null"])
                dist.append("null");
        # print(dist)
        # print(dist1)
        if len(dist1) != 0:
            mini=(min(dist1));
            for i in range(len(dist)):
                if dist[i]==mini:
                    return i;
        return -1;