class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        #pick type 3 while total cost < type 1 + type 2 and requirements not reached
        total = 0
        have1 = 0
        have2 = 0
        if costBoth < cost1 + cost2:
            units = min(need1, need2)
            total += (costBoth * units)
            need1, need2 = need1 - units, need2 - units

        cost1 = min(cost1, costBoth)
        cost2 = min(cost2, costBoth)

        return total + (need1 - have1) * cost1 + (need2 - have2) * cost2

        