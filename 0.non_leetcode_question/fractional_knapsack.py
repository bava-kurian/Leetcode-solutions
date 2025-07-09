def fractionalknapsack(W, arr, n):
    # Sort items by value/weight ratio in descending order
    arr.sort(key=lambda x: x[0]/x[1], reverse=True)

    rem = W
    output = 0

    for item in arr:
        if rem == 0:
            break
        value, weight = item
        take = min(rem, weight)
        output += take * (value / weight)
        rem -= take

    return output

arr = [[70, 10], [90, 20], [150, 30]]
print(fractionalknapsack(25, arr, 3))
