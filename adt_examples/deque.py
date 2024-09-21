"""Class Deque."""


class Deque:
    """Class Deque."""

    def __init__(self, size):
        """Define init."""
        self.size = size
        self.ring = [None] * size
        self.head = -1
        self.tail = 0
        self.len = 0

    def append(self, other):
        """Define append."""
        self.ring[self.tail] = other
        self.tail = (self.tail + 1) % self.size
        self.len += 1

    def appendleft(self, other):
        """Define appendleft."""
        self.ring[self.head] = other
        self.head = (self.head - 1) % self.size
        self.len += 1

    def pop(self):
        """Define pop."""
        self.tail = (self.tail - 1) % self.size
        self.len += -1
        value = self.ring[self.tail]
        self.ring[self.tail] = None
        return value

    def popleft(self):
        """Define popleft."""
        self.head = (self.head + 1) % self.size
        self.len += -1
        value = self.ring[self.head]
        self.ring[self.head] = None
        return value

    def peek(self):
        """Define peek."""
        return self.ring[self.tail - 1]

    def peekleft(self):
        """Define peekleft."""
        return self.ring[(self.head + 1) % self.size]

    def __len__(self):
        """Define length."""
        return self.len

    def __iter__(self):
        """Define iterator."""
        return DequeIterator(self)


class DequeIterator:
    """Class the iterator."""

    def __init__(self, deque):
        """Define init."""
        self.dring = deque.ring
        self.dsize = deque.size
        self.dhead = deque.head
        self.count = 0

    def __iter__(self):
        """Define iterator."""
        return self

    def __next__(self):
        """Define next."""
        if self.count < self.dsize:
            self.count += 1
            return self.dring[(self.dhead + self.count) % self.dsize]

        else:
            raise StopIteration
