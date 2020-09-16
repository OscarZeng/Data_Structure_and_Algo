#Sample solution using the greedy algorithm
#The difficulty of greedy algorithm is not implementing it self, but to come up with 
#the idea and prove it works
#the logic here is that when it comes to the first station that can not reach, the last one must provide less oil than it 
#should support for the distance between them. For all the previous points, if it is reachable, the oil remaining in the 
#tank the worst case will be 0. Hence, if at this point is not reachable, for all the points in front as a starting point,
#it will not be able to be the starting point

#To check whether the there is a point has the following logic: if the total oil in the tank is less than the total cost, 
#There must not be any possible
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1

作者：LeetCode
链接：https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#O(N) solution with low effciency
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        check = 0
        while check < len(gas):
            #Do the checking
            if self.checkComplete(gas, cost):
                return check
            gasFirst = gas.pop(0)
            costFirst = cost.pop(0)
            gas.append(gasFirst)
            cost.append(costFirst)
            check += 1
        return -1
    
    def checkComplete(self,gas, cost):
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                return False
        return True