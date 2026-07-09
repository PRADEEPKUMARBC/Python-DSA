# O(log n) : Reduces the problem size by in each step

def find_name(names, target):
    left = 0
    right = len(names) - 1

    while left <= right:
        mid = (left + right) // 2
        if names[mid] == target:
            return True
        elif names[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


names = ["Alice", "Bob", "Charlie", "David", "Eve"]
target = "Charlie"

result = find_name(names, target)

if result:
    print(f"{target} is in the list of names.")
else:   
    print(f"{target} is not in the list of names.")