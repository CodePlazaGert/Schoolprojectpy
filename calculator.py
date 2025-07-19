import math

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base, exponent):
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, n):
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(n)
        self.history.append(f"√{n} = {result}")
        return result
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers!")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result
    
    def sin(self, x):
        result = math.sin(math.radians(x))
        self.history.append(f"sin({x}°) = {result}")
        return result
    
    def cos(self, x):
        result = math.cos(math.radians(x))
        self.history.append(f"cos({x}°) = {result}")
        return result
    
    def tan(self, x):
        result = math.tan(math.radians(x))
        self.history.append(f"tan({x}°) = {result}")
        return result
    
    def log(self, n, base=10):
        if n <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers!")
        result = math.log(n, base)
        self.history.append(f"log{base}({n}) = {result}")
        return result
    
    def natural_log(self, n):
        if n <= 0:
            raise ValueError("Natural logarithm is not defined for non-positive numbers!")
        result = math.log(n)
        self.history.append(f"ln({n}) = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            print("No calculations in history.")
            return
        print("\n--- Calculation History ---")
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
    
    def clear_history(self):
        self.history.clear()
        print("History cleared.")

def display_menu():
    print("\n=== calculator for school ===")
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (×)")
    print("4.  Division (÷)")
    print("5.  Power (^)")
    print("6.  Square Root (√)")
    print("7.  Factorial (!)")
    print("8.  Sin (degrees)")
    print("9.  Cos (degrees)")
    print("10. Tan (degrees)")
    print("11. Logarithm (base 10)")
    print("12. Natural Logarithm (ln)")
    print("13. Show History")
    print("14. Clear History")
    print("15. Exit")
    print("=" * 25)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    calc = Calculator()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-15): ").strip()
        
        try:
            if choice == '1':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"Result: {result}")
            
            elif choice == '2':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"Result: {result}")
            
            elif choice == '3':
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"Result: {result}")
            
            elif choice == '4':
                a = get_number("Enter dividend: ")
                b = get_number("Enter divisor: ")
                result = calc.divide(a, b)
                print(f"Result: {result}")
            
            elif choice == '5':
                base = get_number("Enter base: ")
                exp = get_number("Enter exponent: ")
                result = calc.power(base, exp)
                print(f"Result: {result}")
            
            elif choice == '6':
                n = get_number("Enter number: ")
                result = calc.square_root(n)
                print(f"Result: {result}")
            
            elif choice == '7':
                n = int(get_number("Enter integer: "))
                result = calc.factorial(n)
                print(f"Result: {result}")
            
            elif choice == '8':
                angle = get_number("Enter angle in degrees: ")
                result = calc.sin(angle)
                print(f"Result: {result}")
            
            elif choice == '9':
                angle = get_number("Enter angle in degrees: ")
                result = calc.cos(angle)
                print(f"Result: {result}")
            
            elif choice == '10':
                angle = get_number("Enter angle in degrees: ")
                result = calc.tan(angle)
                print(f"Result: {result}")
            
            elif choice == '11':
                n = get_number("Enter number: ")
                base = input("Enter base (press Enter for base 10): ").strip()
                if base == "":
                    result = calc.log(n)
                else:
                    result = calc.log(n, float(base))
                print(f"Result: {result}")
            
            elif choice == '12':
                n = get_number("Enter number: ")
                result = calc.natural_log(n)
                print(f"Result: {result}")
            
            elif choice == '13':
                calc.show_history()
            
            elif choice == '14':
                calc.clear_history()
            
            elif choice == '15':
                print("Thank you for using the calculator!")
                break
            
            else:
                print("Invalid choice! Please select a number between 1-15.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()