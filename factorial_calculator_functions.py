def get_non_negative_integer() -> int:
    """Prompt the user for a valid non-negative integer."""
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n >= 0:
                return n
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")

def calculate_factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main() -> None:
    """Get user input, calculate the factorial, and display the result."""
    number = get_non_negative_integer()
    print(f"The factorial of {number} is: {calculate_factorial(number)}")

if __name__ == "__main__":
    main()
