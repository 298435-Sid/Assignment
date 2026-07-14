def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

arr = [10, 20, 30, 40, 50, 60]
target = 50

index = binary_search(arr, target, 0, len(arr) - 1)

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found")