import heapq
from heapq import heappop, heappush
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_pack = []
        sell_pack = []
        for p,a,t in orders:
            if t == 0:
                #采购订单
                while a and sell_pack and sell_pack[0][0] <= p:
                    x, y = heappop(sell_pack)
                    if a >= y:
                        a -= y
                    else:
                        heappush(sell_pack,(x, y-a))
            else:
                #销售订单
                pass
