def number_to_words(number):
    # Define word representations for numbers from 0 to 19
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    # Define word representations for tens from 20 to 90
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    # Convert numbers less than 20 directly to their word representation
    if number < 20:
        return ones[number]

    # Convert numbers between 20 and 99
    if number < 100:
        # Get the tens part and ones part of the number separately
        return tens[number // 10] + ('' if number % 10 == 0 else '-' + ones[number % 10])

    # Convert numbers between 100 and 999
    if number < 1000:
        # Get the hundreds part and the remaining two digits separately
        return ones[number // 100] + ' hundred' + ('' if number % 100 == 0 else ' and ' + number_to_words(number % 100))

    # Convert numbers between 1000 and 999999
    if number < 1000000:
        # Get the thousands part and the remaining digits separately
        return number_to_words(number // 1000) + ' thousand' + ('' if number % 1000 == 0 else ', ' + number_to_words(number % 1000))

    # Convert numbers between 1000000 and 999999999
    if number < 1000000000:
        # Get the millions part and the remaining digits separately
        return number_to_words(number // 1000000) + ' million' + ('' if number % 1000000 == 0 else ', ' + number_to_words(number % 1000000))

    # Return "Number out of range" if the input number is too large
    return "Number out of range"

# Example usage:
while True:
    try:
        user_input = int(input("Enter a number between 1 and 999999999 (or -1 to exit): "))
        if user_input == -1:
            break
        elif 1 <= user_input <= 999999999:
            print(number_to_words(user_input))
        else:
            print("Number out of range, please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Explanation:
#tens[number // 10]   # This part retrieves the word representation of the tens place digit.
                    # The division (//) by 10 gets the tens place digit of the input number,
                    # and then tens[] (the list of word representations for tens) is used to get the corresponding word.

#+  # The plus symbol is used to concatenate (combine) two strings together.

#('' if number % 10 == 0 else '-' + ones[number % 10])
# This part retrieves the word representation of the ones place digit (when it's not zero) and combines it with a hyphen ('-')
# to separate the tens and ones place words when the ones place digit is not zero.

# Explanation of the ternary conditional expression (also known as the ternary operator):
# ('' if number % 10 == 0 else '-' + ones[number % 10])
# The ternary conditional expression is used to provide a compact way to write a conditional statement with a single expression.
# In this case, it checks whether the ones place digit is zero or not (number % 10 == 0).
# If it's zero, an empty string ('') is returned (since we don't want a hyphen in this case).
# If it's not zero, a hyphen ('-') is concatenated with the word representation of the ones place digit obtained from ones[number % 10].

# Overall, this expression combines the word representations of the tens and ones place digits,
# with a hyphen in between if the ones place digit is not zero.

# Example usage and user input handling:
while True:  # This starts an infinite loop to keep asking for input until the user enters -1 to exit.

    try:  # This block handles potential exceptions raised during user input.
        user_input = int(input("Enter a number between 1 and 999999999 (or -1 to exit): "))
        # The user is prompted to input a number, and it's converted to an integer using int().

        if user_input == -1:  # If the user enters -1, the loop breaks, and the program exits.
            break

        elif 1 <= user_input <= 999999999:  # If the input is within the allowed range:
            print(number_to_words(user_input))
            # The number_to_words function is called to convert the input number into its word representation,
            # and the result is printed to the console.

        else:  # If the input number is outside the allowed range (less than 1 or greater than 999999999):
            print("Number out of range, please try again.")
            # An error message is printed to the console, and the loop continues to ask for valid input.

    except ValueError:  # If the input cannot be converted to an integer (e.g., non-numeric input):
        print("Invalid input. Please enter a valid number.")
        # An error message is printed to the console, and the loop continues to ask for valid input.


