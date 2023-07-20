def test_1_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4

    dp = [0 for i in range(bagWeight+1)]
    for j in range(len(dp)):
        if weight[0] > j:
            dp[j]=0
        else:
            dp[j] = value[0]

    for i in range(1,len(weight)):
        for j in range(len(dp)-1,-1,-1):
            if weight[i] > j:
                dp[j] = dp[j]
            else:
                dp[j] = max(dp[j],dp[j-weight[i]]+value[i])
    print(dp)

print(test_1_wei_bag_problem())