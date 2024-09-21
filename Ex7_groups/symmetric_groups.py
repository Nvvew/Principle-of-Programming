"""Class SymmetricGroup."""
from example_code import groups
import numpy as np

class SymmetricGroup(groups.Group):
    """Symmetric Group."""

    symbol = "S"

    def _validate(self, value):
        """Define validation."""
        if not (isinstance(value, np.ndarray) and
                sorted(value) == list(range(0, self.n))):
            raise ValueError("Element Value must be an array from"
                             f"0 to {self.n}")

    def operation(self, a, b):
       """Perform the group operation on two values."""
           
       return (a[b])
