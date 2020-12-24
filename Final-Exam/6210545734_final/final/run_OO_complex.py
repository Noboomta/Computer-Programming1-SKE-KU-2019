import OO_complex
import OO_fraction

def test_complex_op(x, y):
    print("First operand: ", end='')
    print(x)
    print("Second operand: ", end='')
    print(y)
    print("First + Second = ", end='')
    print(x + y)
    print("Second + First = ", end='')
    print(y + x)
    print("First - Second = ", end='')
    print(x - y)
    print("Second - First = ", end='')
    print(y - x)
    print("First * Second = ", end='')
    print(x * y)
    print("Second * First = ", end='')
    print(y * x)

x = OO_complex.Complex(5.0, 6.0)
y = OO_complex.Complex(-3.0, 4.0)
test_complex_op(x, y)
print()

# 1/2 + 1/3j
x1 = OO_fraction.Fraction(1, 2)
y1 = OO_fraction.Fraction(1, 3)
c1 = OO_complex.Complex(x1, y1)
test_complex_op(c1, c1)
print()
# 1/3 + 1/6j
x2 = OO_fraction.Fraction(1, 3)
y2 = OO_fraction.Fraction(1, 6)
c2 = OO_complex.Complex(x2, y2)
test_complex_op(c2, c2)
print()
test_complex_op(c1, c2)


