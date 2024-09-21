"""Class Verified Sets."""
import numbers 

class VerifiedSet(set):
    """Class Verified Sets."""
    def _verify(self, value):
        raise NotImplementedError
    
    """
    def __init__(self, value):
        raise NotImplementedError
    """

    def add(self, value):
        if self._verify(value):
            super().add(value)
    
    def update(self, other):
        for n in other:
            if self._verify(n):
                super().add(n)
    
    def symmetric_difference_update(self, other):
        v = set()
        for n in other:
            if self._verify(n):
                v.add(n)
        super().symmetric_difference_update(v)
    
    def union(self, other):
        v = set()
        for n in other:
            if self._verify(n):
                v.add(n)
        b = super().union(v)
        self.symmetric_difference_update(self)
        self.update(b)
        return(self)
    
    def intersection(self, other):
        v = set()
        for n in other:
            if self._verify(n):
                v.add(n)
        b = super().intersection(v)
        self.symmetric_difference_update(self)
        self.update(b)
        return(self)
    
    def difference(self, other):
        v = set()
        for n in other:
            if self._verify(n):
                v.add(n)
        b = super().difference(v)
        self.symmetric_difference_update(self)
        self.update(b)
        return(self)
    
    def symmetric_difference(self, other):
        v = set()
        for n in other:
            if self._verify(n):
                v.add(n)
        b = super().symmetric_difference(v)
        self.symmetric_difference_update(self)
        self.update(b)
        return(self)
    
    def copy(self):
        return self
    

class IntSet(VerifiedSet):
    def _verify(self, value):
        if isinstance(value, numbers.Integral):
            return True
        else:
            raise TypeError(
                f"IntSet expected an integer, got a {type(value)}"
            )


class UniquenessError(KeyError):
    pass


class UniqueSet(VerifiedSet):
    def _verify(self, value):
        if not value in self:
            return True
        else:
            raise UniquenessError(
                "The operation would add a duplicate value to the UniqueSet."
            )

