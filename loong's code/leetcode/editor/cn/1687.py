def boxDelivering(boxes: list[list[int]], portsCount: int,
                  maxBoxes: int, maxWeight: int) -> int:
    path = 0
    weight = 0
    flag = 0
    Dict = []

    List = [[] for _ in range(1)]
    List[0] = boxes[0]
    for i in range(1, len(boxes)):
        if boxes[i][0] == boxes[i - 1][0]:
            List.append(boxes[i])
        else:
            Dict.append(List)
            List = [[] for _ in range(1)]
            List[0] = boxes[i]
    else:
        Dict.append(List)
    print(Dict)
    package = []
    for i in Dict:
        for j in range(len(i)):
            x = i[j]
            if weight + i[j][-1] <= maxWeight:
                weight += i[j][-1]
                package.append(i[j])
            else:
                package = []
                flag += 2
                weight = i[j][-1]
                package.append(i[j])
        else:
            if package:
                flag += 2
                weight = 0
                package = []
    print(flag)


boxDelivering([[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3], [5, 2]], portsCount=5, maxBoxes=5,
              maxWeight=7)
