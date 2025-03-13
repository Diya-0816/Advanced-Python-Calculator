from calculator.operations import Calculator
from calculator.history import CalculationHistory
from calculator.logger import Logger

def repl():
    calc = Calculator()
    history = CalculationHistory()
    
    print("Advanced Python Calculator (Type 'exit' to quit)")
    print("Commands: 'history' to view, 'clear' to delete all, 'delete' to remove last entry")

    while True:
        try:
            user_input = input("Enter calculation (e.g., 2 + 2): ").strip()
            if user_input.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                Logger.log_info("User exited the calculator.")
                break
            elif user_input.lower() == 'history':
                print(history.load_history())
                Logger.log_info("User viewed calculation history.")
                continue
            elif user_input.lower() == 'clear':
                history.clear_history()
                print("Calculation history cleared.")
                Logger.log_info("User cleared calculation history.")
                continue
            elif user_input.lower() == 'delete':
                print(history.delete_last_entry())
                Logger.log_info("User deleted the last entry in history.")
                continue

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format! Use: <num1> <operator> <num2> (e.g., 3 + 2)")
                Logger.log_error(f"Invalid input format: {user_input}")
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
                Logger.log_error(f"Invalid operator used: {operator}")
                continue

            print(f"Result: {result}")
            history.save_calculation(num1, operator, num2, result)  # Save to history
            Logger.log_info(f"User performed calculation: {num1} {operator} {num2} = {result}")

        except ValueError as ve:
            print(f"Input Error: {ve}")
            Logger.log_error(f"ValueError: {ve}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            Logger.log_error(f"Unexpected Error: {e}")

if __name__ == "__main__":
    repl()