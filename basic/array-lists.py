from typing import Optional, Any
import array

# Lists
numbers: list[int] = [1, 2, 3, 4, 5]
fruits: list[str] = ["apple", "banana", "cherry"]
mixed: list[Any] = [1, "apple", 3.14, True]

print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed:", mixed)

# Arrays
int_array: array.array = array.array('i', [1, 2, 3, 4, 5])