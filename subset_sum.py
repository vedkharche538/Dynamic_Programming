import numpy as np
def subset_sum(arr, arr_sum) -> bool:
    n = len(arr)

    # Initialization
    t = np.zeros((n+1, arr_sum+1), dtype=bool)

    for i in range(n+1):
        t[i][0] = True

    for j in range(1, arr_sum+1):
        t[0][j] = False

    for i in range(1,n+1):
        for j in range(1, arr_sum + 1):
            if j <= arr[i-1]:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    return t[n][arr_sum]

print(subset_sum([1,1,2,3], 4))