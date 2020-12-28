# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

t = int(input())


def find_pivot_using_bs(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((high + low) / 2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[mid] <= arr[low]:
        return find_pivot_using_bs(arr, low, mid - 1)
    return find_pivot_using_bs(arr, mid + 1, high)


def find_rotations(arr, n):
    pivot = find_pivot_using_bs(arr, 0, n - 1)
    if pivot == -1 or pivot == n - 1:
        return 0
    return pivot + 1


for tc in range(t):
    arr = list(map(int, input().strip().split()))
    print(find_rotations(arr, len(arr)))
