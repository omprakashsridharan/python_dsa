# https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/

arr = list(map(int, input().strip().split()))
n = len(arr)
arr_sum = 0
curr_max = 0
for i in range(0, n):
    curr_max = curr_max + i * arr[i]
    arr_sum = arr_sum + arr[i]
max_val = curr_max
for j in range(1, n):
    curr_max = curr_max + arr_sum - (n * arr[n - j])
    if max_val < curr_max:
        max_val = curr_max
print(max_val)