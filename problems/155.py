class Node:
    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val
        self.prev = None
        self.next = None

    def __repr__(self):
        return self.val


class MinStack:
    def __init__(self):
        self.tail: Node | None = None

    def push(self, val: int) -> None:
        if self.tail == None:
            self.tail = Node(val, val)
        else:
            if val < self.tail.min_val:
                self.tail.next = Node(val, val)
            else:
                self.tail.next = Node(val, self.tail.min_val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def pop(self) -> None:
        if self.tail.prev == None:
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def top(self) -> int:
        return self.tail.val

    def getMin(self) -> int:
        return self.tail.min_val
