def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums = [45, 12, 78, 23, 56, 89, 34]

print(linear_search(nums, 23))  # Output: 3