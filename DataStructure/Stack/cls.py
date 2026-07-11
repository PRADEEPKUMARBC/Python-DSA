class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print("Stack (top > bottom):", self.items[::-1])
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("After pushing 10, 20, 30")
s.display()

print("Top Element", s.peek())
print("Popped Element", s.pop())
print("After Element",)
s.display()
print("Total Size", s.size())
print("Is Stack Is Empty",s.is_empty())