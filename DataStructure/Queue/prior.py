import heapq

hospital = []
#lower number = higher priority
heapq.heappush(hospital, (3, "Broken Finger"))
heapq.heappush(hospital, (1, "Heart Attack"))
heapq.heappush(hospital, (2, "High Fever"))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))

# heapq.heappush(queue, item)