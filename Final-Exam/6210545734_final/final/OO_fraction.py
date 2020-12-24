class Fraction:
    def __init__(self, num, den):
        """To add check if den is zero"""
        """To add check if num and den are both integers"""
        self.num = num
        self.den = den

    @staticmethod
    def __gcd(a, b):
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def reduce(self):
        g = self.__gcd(self.num, self.den)
        return Fraction(self.num//g, self.den//g)

    def add(self, m):
        f_num = self.num*m.den + m.num*self.den
        f_den = self.den*m.den
        f = Fraction(f_num, f_den)
        return f.reduce()

    def __add__(self, m):
        return self.add(m)

    def negate(self):
        return Fraction(-self.num, self.den)

    def subtract(self, m):
        f = m.negate()
        return self.add(f)
    
    def __sub__(self, m):
        return self.subtract(m)
    
    def multiply(self, n):
        f_num = self.num*n.num
        f_den = self.den*n.den
        f = Fraction(f_num, f_den)
        return f.reduce()
    
    def __mul__(self, n):
        return self.multiply(n)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
