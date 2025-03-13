class CalculatorError(Exception):
    """Base class for exceptions in this calculator."""
    pass

class InvalidInputError(CalculatorError):
    """Raised when the user inputs an invalid calculation format."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""
    pass 
