class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        zuobiao = [51, 51]
        x = y = maxweight = -1
        for i in range(0, 51):
            for j in range(0, 51):
                weight = 0
                for k in towers:
                    weight2 = 0
                    distance = pow(((k[0] - i) ** 2) + ((k[1] - j) ** 2), 0.5)
                    if distance <= radius:
                        weight2 = k[2] / (1 + distance)
                    weight += int(weight2)
                if weight > maxweight:
                    maxweight = weight
                    x = i
                    y = j
        return [x, y]

    # for i in range(0, 51):
    #     for j in range(0, 51):
    #         weight = 0
    #         for k in towers:
    #             weight2 = 0
    #             distance = pow((k[0] - i) ** 2 + (k[1] - j) ** 2, 0.5)
    #             if distance <= radius:
    #                 weight2 = k[2] / (1 + distance)
    #             weight += int(weight2)
    #             if weight == maxweight:
    #                 if i < zuobiao[0]:
    #                     zuobiao[0] = i
    #                     zuobiao[1] = j
    #                 if i == zuobiao[0]:
    #                     if j < zuobiao[1]:
    #                         zuobiao[0] = i
    #                         zuobiao[1] = j




class Solution:
    towers = [[2,1,9],[0,1,9]]
    radius = 2
    print(bestCoordinate(towers, radius))
