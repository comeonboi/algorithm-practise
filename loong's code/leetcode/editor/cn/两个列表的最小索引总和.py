from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurant = {}
        indexDict = {}
        ans = []
        ans2 = []
        index1 = {}
        for i in list1:
            if i not in restaurant:
                restaurant[i] = 1
            else:
                restaurant[i] += 1
            if i not in indexDict:
                indexDict[i] = list1.index(i)
            else:
                indexDict[i] += list1.index(i)
        for i in list2:
            if i not in restaurant:
                restaurant[i] = 1
                indexDict[i] = list2.index(i)
            else:
                restaurant[i] += 1
            if i not in indexDict:
                indexDict[i] = list2.index(i)
            else:
                indexDict[i] += list2.index(i)
        maxNum = max(restaurant.values())
        # 找是出现次数最多的餐厅，然后把他的索引计数单独存一个hash
        for i in restaurant:
            if restaurant[i] == maxNum:
                ans.append(i)
        for i in ans:
            index1[i] = indexDict[i]
        minIndex = min(index1.values())
        for i in ans:
            if indexDict[i] == minIndex:
                ans2.append(i)
        return ans2
print(Solution.findRestaurant(Solution(),list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
                              , list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))


