from calculator.operations import Calculator
from calculator.history import CalculationHistory
from calculator.logger import Logger
from calculator.exceptions import InvalidInputError, DivisionByZeroError

def repl():
    calc = Calculator()
    history = CalculationHistory()

    Logger.log_info("Calculator REPL started.")

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
                history_data = history.load_history()
                print(history_data)
                Logger.log_info(f"User viewed calculation history: {history_data.shape[0]} entries")
                continue
            elif user_input.lower() == 'clear':
                history.clear_history()
                print("Calculation history cleared.")
                Logger.log_info("User cleared calculation history.")
                continue
            elif user_input.lower() == 'delete':
                msg = history.delete_last_entry()
                print(msg)
                Logger.log_info(msg)
                continue

            parts = user_input.split()
            if len(parts) != 3:
                Logger.log_error(f"Invalid input format: {user_input}")
                raise InvalidInputError("Invalid format! Use: <num1> <operator> <num2> (e.g., 3 + 2)")

            num1, operator, num2 = parts
            try:
                num1, num2 = float(num1), float(num2)
            except ValueError:
                print("Invalid numbers entered!")
                Logger.log_error(f"Invalid number input: {user_input}")
                continue

            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                try:
                    result = calc.divide(num1, num2)
                except DivisionByZeroError as e:
                    print(f"Error: {e}")
                    Logger.log_error(f"Division by zero error: {e}")
                    continue
            else:
                print("Invalid operator! Use +, -, *, or /")
                Logger.log_error(f"Invalid operator used: {operator}")
                continue

            print(f"Result: {result}")
            history.save_calculation(num1, operator, num2, result)
            Logger.log_info(f"User performed calculation: {num1} {operator} {num2} = {result}")

        except InvalidInputError as e:
            print(f"Input Error: {e}")
            Logger.log_error(f"Invalid input error: {e}")

        except Exception as e:
            print(f"Unexpected Error: {e}")
            Logger.log_error(f"Unexpected Error: {e}")

if __name__ == "__main__":
    repl()