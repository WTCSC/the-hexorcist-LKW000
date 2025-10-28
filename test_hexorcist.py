import pytest

from the_hexorcist import string_to_int, to_decimal, from_decimal, DIGITS

def test_hexorcist():
    """
    Runs simple tests for all core conversion function.
    """
    print("...Running test suite...")
    print("\nTesting string_to_int...")
    
    assert string_to_int("10") == 10, "to_decimal failed for '10'"
    assert string_to_int("36") == 36, "string_to_int failed for '36'"
    assert string_to_int("12345") == 12345, "string_to_int failed for '12345'"
    
    print("\nTesting to_decimal...")
    
    assert to_decimal("123", 10) == 123, "to_decimal failed for Base-10"
    assert to_decimal("1010", 2) == 10, "to_decimal failed for Base-2"
    assert to_decimal("A", 16) == 10, "to_decimal failed for Base-16 'A'"
    assert to_decimal('F', 16) == 15, "to_decimal failed for Base-16 'F'"
    assert to_decimal("1A", 16) == 26, "to_decimal failed for Base-16 '1A'(1*16 + 10)"
    assert to_decimal("Z", 36) == 35, "to_decimal failed for Base-36 'Z'"
   
    assert to_decimal("23", 5) == 13, "to_decimal failed for Base-5 '23'"
  
    print("\nTesting from_decimal...")
    assert from_decimal(123, 10) == "123", "from_decimal failed for Base-10"
    assert from_decimal(10, 2) == "1010", "from_decimal failed for Base-2"
    assert from_decimal(10, 16) == "A", "from_decimal failed for Base-16 '10'"
    assert from_decimal(26, 16) == "1A", "from_decimal failed for Base-16 '26'"
    assert from_decimal(0, 10) == "0", "from_decimal failed for Zero"
    assert from_decimal(35, 36) == "Z", "from_decimal failed for Base-36 '35'"
     
    print("\nTesting full round trip (Base-16 -> Base-10 -> Base-2)...")
    
    hex_num = "1F" 
    base_10 = to_decimal(hex_num, 16) 
    base_2 = from_decimal(base_10, 2) 
    assert base_10 == 31, "Round trip: Hex to Decimal failed."
    assert base_2 == "11111", "Round trip: Decimal to Binary failed."

    print("\n✅ All tests passed!")