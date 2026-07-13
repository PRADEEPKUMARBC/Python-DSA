todays_orders = ["apple", "banana", "apple", "orange", "banana", "apple"]

def count_orders(orders):
    freq = {}

    for dish in orders:
        if dish in freq:
            freq[dish] += 1
        else:
            freq[dish] = 1
    return freq

order_count = count_orders(todays_orders)
print(order_count)