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
            else:
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
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main() -> None:
    """Main program flow to get the non-negative integer, calculate the factorial, and display the result."""
    number = get_non_negative_integer()  # Get valid input
    result = calculate_factorial(number)  # Calculate the factorial
    print(f"The factorial of {number} is: {result}")  # Display the result

if __name__ == "__main__":
    main()