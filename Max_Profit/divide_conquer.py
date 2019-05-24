### DIVIDE AND CONQUER
def divandconq(arr):
    if len(arr) <= 1:
        return 0;
    div = int(len(arr) / 2)
    left  = arr[:div]
    right = arr[div:]
    leftBest  = divandconq(left)
    rightBest = divandconq(right)
    crossBest = max(right) - min(left)
    return max(leftBest, rightBest, crossBest)
