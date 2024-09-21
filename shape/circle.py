from numbers import Number
class Circle:

    def __init__(self, c, r):
        self.centre = c
        self.radius = r
        
    def __contains__(self, other):
        if isinstance(self, Circle) and isinstance(other, tuple) and len(other) == 2\
        and isinstance(other[0], Number) and isinstance(other[1], Number):
            a = other[0]
            b = other[1]
            if (a - self.centre[0])**2 + (b - self.centre[1])**2 < self.radius**2:
                return True
            else:
                return False
            
        else:
            return NotImplemented

