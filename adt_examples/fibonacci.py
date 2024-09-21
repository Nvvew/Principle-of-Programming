"""Fibonacci module."""


class Fib:
    """Class Fibonacci."""

    def __init__(self):
        """Define init."""
        self.here = 1
        self.next = 1

    def __iter__(self):
        """Define iter."""
        return self

    def __next__(self):
        """Define next."""
        nextfib = self.here + self.next
        self.here = self.next
        self.next = nextfib
        return self.here
