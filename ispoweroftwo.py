def isPowerOfTwo(n):
    try:
        n = float(n)
        if n <= 0:
            return "The number is less than 1. Please enter a number higher than that"

        original_n = n  # Save the original value for the final output
        while n > 1:
            if n % 2 != 0:
                return f"False. The number {original_n} is not a power of two!"
            n /= 2

        return f"True. The number '{original_n}' is a power of two!"
    except ValueError:
        return "That's not a valid number, or it is a string."

# Take input as a string to handle both numeric and string inputs
user_input = input("Enter a number, and we'll check if the number is a power of two: ")
print(isPowerOfTwo(user_input))
