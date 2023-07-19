def test_2_wei_bag_problem1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    dp = [[0 for j in range(bagweight+1)] for i in range(len(value))]
    for j in range(len(dp[0])):
        if j < weight[0]:
            dp[0][j] = 0
        else:
            dp[0][j] = value[0]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[i])):
            if j<weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
    return dp

print(test_2_wei_bag_problem1())

