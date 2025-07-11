class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x:x[0]-x[1])
        total=0
        bound=len(costs)//2
        for i in range(bound):
            total+=costs[i][0]
        for i in range(bound,len(costs)):
            total+=costs[i][1]
        return total

