def has_duplicate_slow(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 3,9, 10]

result = has_duplicate_slow(numbers)
if result == True: 
    print("duplicate is found.")
else:   
    print("There are no duplicates in the list.")