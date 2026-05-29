class Complex:

    def __init__(self, real, imag):

        self.real = real
        self.imag = imag


    def show(self):

        print(f"{self.real} + {self.imag}i")


    def add(self, c2):

        real_part = self.real + c2.real
        imag_part = self.imag + c2.imag

        return Complex(real_part, imag_part)


    def multiply(self, c2):

        real_part = (self.real * c2.real) - (self.imag * c2.imag)

        imag_part = (self.real * c2.imag) + (self.imag * c2.real)

        return Complex(real_part, imag_part)



c1 = Complex(2, 3)
c2 = Complex(4, 5)

print("First Complex Number:")
c1.show()

print("Second Complex Number:")
c2.show()


print("Addition:")
add_result = c1.add(c2)
add_result.show()


print("Multiplication:")
mul_result = c1.multiply(c2)
mul_result.show()