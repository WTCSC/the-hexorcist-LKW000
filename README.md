# HEXORCIST: The Universal Base Transmuter
### What in the Nine Hells is This?
Welcome, fellow digital sorcerer! This little Python script, Hexorcist, is a command-line utility built to exorcise the numerical demons from any base and rebirth them into a new one. Tired of manually converting Hexadecimal to Binary? Let the Hexorcist do the heavy lifting!

In Plain English: This is a Python project that converts numbers between any base from Base 2 (Binary) to Base 36. It does this without relying on Python's built-in int() or str() functions with a base argument—all the tricky math is done manually, step-by-step.

### How It Works (The Core Magic)
The entire spellbook is contained within three core functions:

string_to_int(base_string):

Purpose: Our foundational ritual. This function manually converts a Base-10 number represented as a string (like "36") into an actual Python integer (36). It proves we can't cheat!

to_decimal(number_string, original_base):

Purpose: The main transmutation spell. It takes any number (like "1A" from Base-16) and converts it to its universal, Base-10 integer value (26). This is done using the classic positional notation algorithm.

from_decimal(decimal_value, target_base):

Purpose: The rebirth ritual. It takes the Base-10 integer and converts it to a string representation in the target_base (e.g., 26 becomes "1A"). This is done using the classic division and remainder algorithm.

#### Getting Started (The Incantation)
Prerequisites

You need Python 3 installed. That's it. It's built with minimal dependencies!

#### Execution

Clone the Repository: (Or just ensure hexorcist.py is on your machine).

Cast the Spell: Open your terminal and run the main file.

### Testing (Proving the Magic Works)
No good sorcerer trusts their magic until it's survived a full dungeon crawl! We use tests to ensure every conversion is accurate.

Test Files

test_hexorcist.py: This file contains the automated test suite, using assert statements to check the functions against known, correct conversions (e.g., ensuring to_decimal("10", 2) always equals 2).

#### Running the Tests (Recommended)

This project uses the excellent pytest library for robust testing, especially for catching those tricky ValueError exceptions.

Install pytest:

Bash
pip install pytest
Run the Tests:

Bash
pytest test_hexorcist.py
If you see green dots and a summary of "passed" tests, your magic is stable!
