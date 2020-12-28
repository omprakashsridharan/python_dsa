# https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

arr = list(map(int, input().strip().split()))
sum_required = int(input())
n = len(arr)
l, r = -1, -1
for i in range(0, n - 1):
    if arr[i] > arr[i + 1]:
        l = (i + 1) % n
        r = i
        break
while l != r:
    if arr[l] + arr[r] == sum_required:
        print("TRUE")
        break

    if arr[l] + arr[r] < sum_required:
        l = (l + 1) % n
    else:
        r = (n + r - 1) % n
