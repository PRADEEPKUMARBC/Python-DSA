def bubble_sort(prices):
    n = len(prices)

    for i in range(n):
        for j in range(0, n - i - 1):

            if prices[j] > prices[j + 1]:
                prices[j], prices[j + 1] = prices[j + 1], prices[j]

    return prices

prices = [64, 34, 25, 12, 22, 11, 90]
sorted_prices = bubble_sort(prices)
print("Sorted prices:", sorted_prices)
    