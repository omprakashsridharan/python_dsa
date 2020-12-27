# Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

t = int(input())
res = []


def binary_search(
    arr,
):
    pass


def find_pivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    return find_pivot(arr, mid + 1, high)


def binary_search(arr, low, high, key):
    if high < low:
        return -1

    mid = int((low + high) / 2)
    if arr[mid] == key:
        return mid
    if arr[mid] < key:
        return binary_search(arr, mid + 1, high, key)
    return binary_search(arr, low, mid - 1, key)


for tc in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    key = int(input())
    pivot_index = find_pivot(arr, 0, n - 1)
    if pivot_index == -1:
        res.append(binary_search(arr, 0, n - 1, key))
        continue
    if arr[pivot_index] == key:
        res.append(pivot_index)
        continue
    if arr[0] <= key:
        res.append(binary_search(arr, 0, pivot_index - 1, key))
    else:
        res.append(binary_search(arr, pivot_index + 1, n - 1, key))

for r in res:
    print(r)
