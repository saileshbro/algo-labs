"""
Takes weights array
Takes profits array
Takes Max Capacity
"""


def greedyFractional(weights, profits, capacity):
    if(capacity <= 0):
        raise Exception("0 Capacity, cannot assign")
    if len(weights) != len(profits):
        raise Exception("Weights and profits should be of same length")
    ratios = [(i, profits[i]/weights[i]) for i in range(0, len(profits))]
    ratios.sort(reverse=True, key=lambda x: x[1])
    totalProfit = 0
    for (i, ratio) in ratios:
        if capacity-weights[i] >= 0:
            capacity -= weights[i]
            totalProfit += profits[i]
        else:
            fraction = capacity/weights[i]
            totalProfit += fraction*profits[i]
            capacity -= fraction*weights[i]
    return totalProfit


def dynamicZeroOne(weights, profits, capacity):
    if(capacity <= 0):
        raise Exception("0 Capacity, cannot assign")
    if len(weights) != len(profits):
        raise Exception("Weights and profits should be of same length")
    dp = [[0 for i in range(capacity+1)]for i in range(len(weights)+1)]
    for i in range(len(weights) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(profits[i-1]
                               + dp[i-1][w-weights[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[len(weights)][capacity]


def bruteforceZeroOne(weights, profits, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if (weights[n-1] > capacity):
        return bruteforceZeroOne(weights, profits, capacity, n-1)
    else:
        return max(profits[n-1] + bruteforceZeroOne(weights, profits, capacity-weights[n-1], n-1),
                   bruteforceZeroOne(weights, profits, capacity, n-1))


def bruteForceFractional(weights, profits, capacity, n):
    maxProfit = 0
    solutions = [format(x, '03b') for x in range(2**n)]
    for sol in solutions:
        i_element = []
        for i, x in enumerate(sol):
            if x == '0':
                i_element.append(i)
        p = sum(int(sol[i])*profits[i] for i in range(n))
        w = sum(int(sol[i])*weights[i] for i in range(n))
        fraction = 0
        if w < capacity:
            for i in i_element:
                if capacity-w < weights[i]:
                    remain = capacity - w
                else:
                    remain = weights[i]
                frac = (profits[i] / weights[i]) * remain
                if frac > fraction:
                    fraction = frac
        p += fraction
        if w <= capacity and p >= maxProfit:
            maxProfit = p
    return int(maxProfit)
