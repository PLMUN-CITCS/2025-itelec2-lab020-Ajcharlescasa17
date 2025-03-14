def get_integer_input() -> int:
    """
    Prompt the user to enter an integer and validate the input.
    
    Returns:
        int: The user's integer input.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


def check_even_odd(number: int) -> str:
    """
    Determine if the given number is even or odd.
    
    Args:
        number (int): The integer to check.
    
    Returns:
        str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."


# Main Program Flow
if __name__ == "__main__":
    user_number = get_integer_input()
    result_message = check_even_odd(user_number)
    print(result_message)