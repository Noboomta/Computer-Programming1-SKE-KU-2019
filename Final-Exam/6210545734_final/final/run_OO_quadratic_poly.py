import OO_complex
import OO_fraction
import OO_quadratic_poly

def test_quadratic_poly_add(x, y):
    print("First operand: ", end='')
    print(x)
    print("Second operand: ", end='')
    print(y)
    print("First + Second = ", end='')
    print(x + y)

def test_quadratic_poly_constant_mult(x, const):
    print("First operand: ", end='')
    print(x)
    print("Constant: ", end='')
    print(const)
    print("Constant * First = ", end='')
    print(x.constant_multiply(const))

c1 = 1
c2 = 2
c3 = 3
c4 = 4
c5 = 5
c6 = 6
qp1 = OO_quadratic_poly.QuadraticPoly(c1, c2, c3)
qp2 = OO_quadratic_poly.QuadraticPoly(c4, c5, c6)
test_quadratic_poly_add(qp1, qp2)
print()
test_quadratic_poly_constant_mult(qp1, c4)
print()


c1 = OO_fraction.Fraction(1, 2)
c2 = OO_fraction.Fraction(1, 3)
c3 = OO_fraction.Fraction(2, 5)
c4 = OO_fraction.Fraction(2, 7)
c5 = OO_fraction.Fraction(5, 4)
c6 = OO_fraction.Fraction(6, 5)
cst = OO_fraction.Fraction(2, 7)
qp1 = OO_quadratic_poly.QuadraticPoly(c1, c2, c3)
qp2 = OO_quadratic_poly.QuadraticPoly(c4, c5, c6)
test_quadratic_poly_add(qp1, qp2)
print()
test_quadratic_poly_constant_mult(qp1, cst)
print()

# First operand: (1.1 + 2.2j)*x^2 + (3.3 + 4.4j)*x + (0.1 + 0.3j)
# Second operand: (5.5 + 6.6j)*x^2 + (7.7 + 8.8j)*x + (1.5 + 1.6j)
# First + Second = (6.6 + 8.8j)*x^2 + (11.0 + 13.200000000000001j)*x + (1.6 + 1.9000000000000001j)

# First operand: (1.1 + 2.2j)*x^2 + (3.3 + 4.4j)*x + (0.1 + 0.3j)
# Constant: 5.5 + 6.6j
# Constant * First = (-8.469999999999999 + 19.36j)*x^2 + (-10.89 + 45.980000000000004j)*x + (-1.4299999999999997 + 2.31j)

c1 = OO_complex.Complex(1.1, 2.2)
c2 = OO_complex.Complex(3.3, 4.4)
c3 = OO_complex.Complex(0.1, 0.3)
c4 = OO_complex.Complex(5.5, 6.6)
c5 = OO_complex.Complex(7.7, 8.8)
c6 = OO_complex.Complex(1.5, 1.6)
cst = OO_complex.Complex(5.5,6.6)
qp1 = OO_quadratic_poly.QuadraticPoly(c1, c2, c3)
qp2 = OO_quadratic_poly.QuadraticPoly(c4, c5, c6)
test_quadratic_poly_add(qp1, qp2)
print()
test_quadratic_poly_constant_mult(qp1, cst)
print()

# First operand: (1/2 + 1/3j)*x^2 + (1/3 + 1/6j)*x + (2/5 + 2/7j)
# Second operand: (1/4 + 1/11j)*x^2 + (3/4 + 3/5j)*x + (5/4 + 6/5j)
# First + Second = (3/4 + 14/33j)*x^2 + (13/12 + 23/30j)*x + (33/20 + 52/35j)

# First operand: (1/2 + 1/3j)*x^2 + (1/3 + 1/6j)*x + (2/5 + 2/7j)
# Constant: 1/4 + 1/11j
# Constant * First = (25/264 + 17/132j)*x^2 + (3/44 + 19/264j)*x + (57/770 + 83/770j)
c1 = OO_complex.Complex(OO_fraction.Fraction(1,2), OO_fraction.Fraction(1,3))
c2 = OO_complex.Complex(OO_fraction.Fraction(1,3), OO_fraction.Fraction(1,6))
c3 = OO_complex.Complex(OO_fraction.Fraction(2,5), OO_fraction.Fraction(2,7))
c4 = OO_complex.Complex(OO_fraction.Fraction(1,4), OO_fraction.Fraction(1,11))
c5 = OO_complex.Complex(OO_fraction.Fraction(3,4), OO_fraction.Fraction(3,5))
c6 = OO_complex.Complex(OO_fraction.Fraction(5,4), OO_fraction.Fraction(6,5))
cst = OO_complex.Complex(OO_fraction.Fraction(1,4), OO_fraction.Fraction(1,11))
qp1 = OO_quadratic_poly.QuadraticPoly(c1, c2, c3)
qp2 = OO_quadratic_poly.QuadraticPoly(c4, c5, c6)
test_quadratic_poly_add(qp1, qp2)
print()
test_quadratic_poly_constant_mult(qp1, cst)
print()