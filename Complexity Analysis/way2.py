def has_duplicate_fast(numbers):
    seen = set() #empty set

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False

numbers = [10,20,30,40,50,10]
