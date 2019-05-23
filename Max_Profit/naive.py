def max_profit_naive(arr):
    pro = []
    days = []
    for i in range(0, len(arr)):
        for j in range (i + 1, len(arr)):
            pro.append(arr[j] - arr[i])
            days.append([arr.index(arr[i])+1 ,arr.index(arr[j])+1])

    print("Buy at day",days[pro.index(max(pro))][0])
    print("Sell at day",days[pro.index(max(pro))][1])
    print("Profit is",max(pro))
