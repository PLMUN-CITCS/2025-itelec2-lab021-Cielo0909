def get_non_negative_integer() -> int:
    """
    Obtains a non-negative integer input from the user.
    Continuously prompts the user until a valid non-negative integer is entered.

    Returns:
        int: The validated non-negative integer entered by the user.
    """
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n >= 0:
                return n
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The calculated factorial of the number.
    """ 