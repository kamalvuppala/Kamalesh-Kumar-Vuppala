class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.strip().lower()

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.a / self.b

    def compute(self):
        if self.operation in ("add", "+"):
            return self.add()
        elif self.operation in ("subtract", "-"):
            return self.subtract()
        elif self.operation in ("multiply", "*"):
            return self.multiply()
        elif self.operation in ("divide", "/"):
            return self.divide()
        else:
            raise ValueError("Invalid operation. Use add/+/subtract/-/multiply/*/divide/.")

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
op = input("Enter operation (add / + / subtract / - / multiply / * / divide / /): ")

calc = Calculator(a, b, op)

try:
    result = calc.compute()
    print("Result:", result)
except Exception as e:
    print("Error:", e)
