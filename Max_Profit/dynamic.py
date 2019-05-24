### DYNAMIC PROGRAMMING

def dynamic_program(arr):
    if len(arr) == 0:
        return 0
    profit = 0
    cheapest = arr[0]
    for i in range(1, len(arr)):
        cheapest = min(cheapest, arr[i])
        profit = max(profit, arr[i] - cheapest)

    return profit
