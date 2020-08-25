class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        General idea: sort array of costs by the difference between costs A and B, so the first have will be cheaper to go to A and the second - to go to B
        1. Sort array of costs by the difference between costs A and B
        2. Calculate sum for A (first half)
        3. Calculate sum for B (second half)
        4. Return sum for A and B
        """
        costs.sort(key=lambda x: x[0]-x[1])
        city_a = sum(x[0] for x in costs[:len(costs)//2])
        city_b = sum(x[1] for x in costs[len(costs) // 2:])
        return city_a + city_b
                
        