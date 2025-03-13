import pandas as pd
import os

HISTORY_FILE = "calculation_history.csv"

class CalculationHistory:
    def __init__(self):
        # Check if history file exists; if not, create an empty one
        if not os.path.exists(HISTORY_FILE):
            df = pd.DataFrame(columns=["num1", "operator", "num2", "result"])
            df.to_csv(HISTORY_FILE, index=False)

    def save_calculation(self, num1, operator, num2, result):
        """Save a calculation to the history file."""
        df = pd.DataFrame([[num1, operator, num2, result]], columns=["num1", "operator", "num2", "result"])
        df.to_csv(HISTORY_FILE, mode="a", header=False, index=False)

    def load_history(self):
        """Load and return the calculation history."""
        if os.path.exists(HISTORY_FILE):
            df = pd.read_csv(HISTORY_FILE)
            return df
        return pd.DataFrame(columns=["num1", "operator", "num2", "result"])

    def clear_history(self):
        """Clear the calculation history."""
        df = pd.DataFrame(columns=["num1", "operator", "num2", "result"])
        df.to_csv(HISTORY_FILE, index=False)

    def delete_last_entry(self):
        """Delete the last calculation entry from history."""
        if os.path.exists(HISTORY_FILE):
            df = pd.read_csv(HISTORY_FILE)
            if not df.empty:
                df = df.iloc[:-1]  # Remove last row
                df.to_csv(HISTORY_FILE, index=False)
                return "Last entry deleted."
        return "No history found."