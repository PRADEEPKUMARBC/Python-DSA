queue = []

queue.append("First")
queue.append("Second")
queue.append("Third")

print(queue)

modlu = queue.pop()
print(modlu)
print(queue)

"""
Double Ended Queue
"""

from collections import deque
queue = deque()

queue.append("Ravi")
queue.append("Shyam")
queue.append("you")
queue.append("Mohan")


print(queue)
