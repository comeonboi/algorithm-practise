from typing import List
import decimal
while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    else:
        if not n:
            break
        list1 = [n]
        for _ in range(m-1):
            n = round(pow(n, 0.5), 2)
            list1.append(n)
            # print(list1)
        print(sum(list1))
