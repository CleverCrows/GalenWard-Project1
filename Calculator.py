class Math:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_first_num(self):
        return self.__a

    def get_second_num(self):
        return self.__b

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def exponential(self, a, b):
        return a ** b

    def integer_divide(self, a, b):
        return a // b

    def modulo(self, a, b):
        return a % b