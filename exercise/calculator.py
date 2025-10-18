from typing import Optional, Any
from utilities import Utilities

# Exercise of Calculator

class Calculator:

    number_selection: Optional[int] = None
    selection: str = ""

    def __init__(self) -> None:
        print("""This is a program of a calculator.
Please select an option:
1. Sum""")

        self.selection = input().strip()
        self.number_selection = Utilities.convert_to_int(self.selection)

        if self.number_selection == 1:
            print("Please enter the first number of the sum: ")
            num: int = Utilities.convert_to_int(input().strip())
            print("Please enter the second number of the sum: ")
            num_2: int = Utilities.convert_to_int(input().strip())

            print("The result of the sum is: ", self.sum(num, num_2))


    @staticmethod
    def sum(num: int, num_2: int) -> int:
        return num + num_2


instance = Calculator()
