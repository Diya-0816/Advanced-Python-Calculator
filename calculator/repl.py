from calculator.operations import Calculator

def repl():
    calc = Calculator()
    print("Advanced Python Calculator (Type 'exit' to quit)")
    
    while True:
        try:
            user_input = input("Enter calculation (e.g., 2 + 2): ").strip()
            if user_input.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break
            
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format! Use: <num1> <operator> <num2> (e.g., 3 + 2)")
                continue

            num1, operator, num2 = parts
            num1, num2 = float(num1), float(num2)

            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                result = calc.divide(num1, num2)
            else:
                print("Invalid operator! Use +, -, *, or /")
                continue

            print(f"Result: {result}")

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    repl() 
