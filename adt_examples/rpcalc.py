"""Class RPCalc."""
from numbers import Number
from math import sin, cos


class RPCalc:
    """Class RPCalc."""

    def __init__(self):
        """Define init."""
        self.stack = []

    def push(self, other):
        """Define push."""
        if isinstance(other, Number):
            self.stack.append(other)

        elif other == "+":
            self.stack.append(self.stack.pop(-1)
                              + self.stack.pop(-1))

        elif other == "-":
            self.stack.append(- self.stack.pop(-1)
                              + self.stack.pop(-1))

        elif other == "*":
            self.stack.append(self.stack.pop(-1)
                              * self.stack.pop(-1))

        elif other == "/":
            self.stack.append(1/(self.stack.pop(-1)
                                 / self.stack.pop(-1)))

        elif other == "sin":
            self.stack.append(sin(self.stack.pop(-1)))

        elif other == "cos":
            self.stack.append(cos(self.stack.pop(-1)))

        else:
            return NotImplemented

    def pop(self):
        """Define pop."""
        return self.stack.pop(-1)

    def peek(self):
        """Define peek."""
        return self.stack[-1]

    def __len__(self):
        """Define length."""
        return len(self.stack)
