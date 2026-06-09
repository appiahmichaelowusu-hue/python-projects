class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Only numbers are allowed")
        return a * b
    
    def add(self,a,b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Only numbers are allowed")
        return a + b 