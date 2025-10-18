from typing import Optional, Any
from utilities import Utilities

# Exercise of Calculator

class Calculator:

    number_selection: Optional[int] = None
    selection: str = ""

    def __init__(self) -> None:
        print("""This is a program of a calculator.
Please select an option:
1. Sum
2. Rest
3. Multiplication
4. Division""")

        self.selection = input().strip()
        self.number_selection = Utilities.convert_to_int(self.selection)

        if self.number_selection == 1:
            print("Please enter the first number of the sum: ")
            num: int = Utilities.convert_to_int(input().strip())
            print("Please enter the second number of the sum: ")
            num_2: int = Utilities.convert_to_int(input().strip())

            print("The result of the sum is: ", self.sum(num, num_2))
        elif self.number_selection == 2:
            print("Please enter the first number of the rest: ")
            num: int = Utilities.convert_to_int(input().strip())
            print("Please enter the second number of the rest: ")
            num_2: int = Utilities.convert_to_int(input().strip())

            print("The result of the rest is: ", self.rest(num, num_2))
        elif self.number_selection == 3:
            print("Please enter the first number of the multiplication: ")
            num: int = Utilities.convert_to_int(input().strip())
            print("Please enter the second number of the multiplication: ")
            num_2: int = Utilities.convert_to_int(input().strip())

            print("The result of the multiplication is: ", self.multiplication(num, num_2))
        elif self.number_selection == 4:
            print("Please enter the first number of the division: ")
            num: int = Utilities.convert_to_int(input().strip())
            print("Please enter the second number of the division: ")
            num_2: int = Utilities.convert_to_int(input().strip())

            print("The result of the division is: ", self.division(num, num_2))


    @staticmethod
    def sum(num: int, num_2: int) -> int:
        return num + num_2

    @staticmethod
    def rest(num: int, num_2: int) -> int:
        return num - num_2

    @staticmethod
    def multiplication(num: int, num_2: int) -> int:
        return num * num_2

    @staticmethod
    def division(num: int, num_2: int) -> int | float:
        return num / num_2


instance = Calculator()
