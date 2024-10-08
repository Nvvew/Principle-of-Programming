from numbers import Number, Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + tuple(-x for x in other.coefficients[common:])

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented
        
    def __rsub__(self,other):
            coefs = (other - self.coefficients[0],)
            coefs += tuple(-a for a in self.coefficients[1:])
            return Polynomial(coefs)
    
    def __mul__(self,other):
        
        if isinstance(other, Polynomial):
            coefs = [0]*(self.degree()+other.degree() + 1)
            for i1 in range(0, self.degree() + 1):
                for i2 in range(0, other.degree() + 1):
                    d = i1 + i2
                    coefs[d] += self.coefficients[i1]*other.coefficients[i2]
            return Polynomial(tuple(coefs))
    
        elif isinstance(other, Number):
            coefs=tuple(other*a for a in self.coefficients)
            return Polynomial(coefs)
        
        else:
            return NotImplemented
        
    def __rmul__(self,other):
        return self*other

    def __pow__(self, other):
        
        if isinstance(other, Integral) and other > 0:
            pi = 1 
            for n in range(0,other):
                pi = pi*self
            return pi
        
        else:
            return NotImplemented

    def __call__(self, other):
        
        if isinstance(other, Integral) and isinstance(self, Polynomial):
            result = 0
            for n in range(0, self.degree() + 1):
                result += self.coefficients[n]*other**n
            return result
        
        else:
            return NotImplemented

    def dx(self):
        
        if isinstance(self, Polynomial):
            coefs = []
            for n in range(0, self.degree()):
                coefs.append(self.coefficients[n + 1]*(n + 1))
            if coefs == [0]*self.degree():
                coefs = [0]
            return Polynomial(tuple(coefs))
        
        else:
            return NotImplemented









def derivative(self):
    
    if isinstance(self, Polynomial):
        return self.dx()
    
    else:
        return NotImplemented

    
