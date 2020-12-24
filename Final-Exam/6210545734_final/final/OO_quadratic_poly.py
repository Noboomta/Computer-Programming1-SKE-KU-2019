from OO_fraction import *
class QuadraticPoly:
    """This is a class for quadratic polynomial that has the form

    (a)*x^2 + (b)*x + (c)

    where a, b, and c are coefficients, x is a variable, and the ^ symbol stands for exponentiation, i.e., x^3 = x*x*x.

    The coefficients all have to be the same type, which can be Complex, Fraction, integer, float, or any type that supports basic arithmetic operations such as addition, subtraction, or multiplication.
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self, other):
        """Return a new quadratic polynomial where coefficients of the terms with the same degree are added together. For example:

        if self is (1)*x^2 + (2)*x + (3) and other is (4)*x^2 + (5)*x + (6), then self.add(other) is (5)*x^2 + (7)*x + (9)
        """
        new_a = self.a + other.a
        new_b = self.b + other.b
        new_c = self.c + other.c
        new = QuadraticPoly(new_a, new_b, new_c)
        return new

    def __add__(self, other):
        return self.add(other)
    
    def constant_multiply(self, const):
        """Return a new quadratic polynomial where each coefficient is multiplied by a constant given in const. """
        new_a = self.a *const
        new_b = self.b *const
        new_c = self.c *const
        new = QuadraticPoly(new_a, new_b, new_c)
        return new

    def __str__(self):
        return f"({self.a})*x^2 + ({self.b})*x + ({self.c})"
