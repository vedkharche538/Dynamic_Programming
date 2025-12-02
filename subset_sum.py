import numpy as np
def subset_sum(arr, arr_sum) -> bool:
    n = len(arr)

    # Initialization
    t = np.zeros((n+1, arr_sum+1), dtype=int)
    for i in range(n+1):
        t[i][0] = 1
    for i in range(1,n+1):
        for j in range(1, arr_sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    return t[n][arr_sum]

print(subset_sum([1,1,1,1,1],4))
