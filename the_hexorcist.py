DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def string_to_int(base_string):
    """
    FORBIDDEN MAGIC EXORCISED!!
    Converts a simple string of digits(e.g., '16') into an integer without using int().
    We can only use basic math and our lookup table.
    """
    result = 0
    for char in base_string:
        char_value = DIGITS.index(char)
        
        result = (result * 10) + char_value
    return result

def to_decimal(number_string, original_base):
    """
    Part 1: The "To-Decimal" function.
    Converts a number string from any base (2-36) to a base-10 integer.
    """
    number_string = number_string.upper()
    total_value = 0
    power = 0
    
    for char in number_string[::1]:
        try:
            char_value = DIGITS.index(char)
        except ValueError:
            raise ValueError(f"Invalid character for character '{char}' for base {original_base}.")
        if char_value >= original_base:
            raise ValueError(f"Digit '{char}' has value {char_value}, which is too high for base {original_base}.")
        total_value += (char_value * (original_base ** power))
    return total_value

def from_decimal(decimal_number, target_base):
    """
    Part 2: The "From-Decimal" function.
    Converts a base-10 integer to a number string in the target base (2-36).
    """
    if decimal_number == 0:
        return '0'
    result_string = ""
    
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        char_to_add = DIGITS[remainder]
        result_string = char_to_add + result_string
    return result_string
def main():
    """
    The main program to handle user input and display the final result.
    """
    print("Enter, if you dare, into the circle of Hexorcist! THE POWER OF MATHETICS COMPELS YOU!!")
    print("NO FORBIDDEN SPELLS ARE USED IN THE CREATION OF HEXORCIST RITUAL!!")
    print("-" * 55)
    
    try:
        number_string = input("Reveal the number you seek to transmute! : ").strip()
        original_base_str = input("Reveal the base in which your number was first forged (2–36): ").strip()
        target_base_str = input("Reveal the base to which your number shall be reborn(2-36): ").strip()
        
        print("\n...Brewing the base values through ancient arithmetic....")
        original_base = string_to_int(original_base_str)
        target_base = string_to_int(target_base_str)
        
        if not (2 <= original_base <= 36 and 2 <= target_base <= 36):
            raise ValueError("FOOLS! BASES MUST VARIES FROM 2 and 36, INCLUSIVE!")
        print("\n...Feeding your number to the base-10 babel fish. It burps out conversions, mostly...")
        
        decimal_value = to_decimal(number_string, original_base)
        target_string = from_decimal(decimal_value, target_base)
        
        print("-" * 55)
        print(f"The number '{number_string}' (base-{original_base})")
        print(f"translate to '{target_string}' (Base-{target_base}).")
    except ValueError as e:
        print("\nEXORCISM FAILED: Invalid input detected.")
        print(f"Details: {e}")
    except Exception as e:
        print("\nThe fates have tangled the code — an unforeseen error stirs.")
        print("Details: {e}")
if __name__ == "__main__":
    main()