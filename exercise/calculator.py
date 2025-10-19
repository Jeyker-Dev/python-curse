from typing import Optional,Callable, Tuple, Any
from utilities import Utilities

# Exercise of Calculator

class Calculator:

    MENU: str = "This is a program of a calculator. \n Please select an option: \n 1. Sum \n 2. Rest \n 3. Multiplication \n 4. Division"

    def __init__(self) -> None:
        self.selection: int | str = ""
        self.number_selection: int | None = None

        print(self.MENU)

        try:
            self.selection = input().strip()
            self.number_selection = Utilities.convert_to_int(self.selection)
        except ValueError:
            print("Invalid Option")
            return

        operations: dict[int, Tuple[Callable[[int, int], int | float], str]] = {
            1: (self.sum, "sum"),
            2: (self.rest, "rest"),
            3: (self.multiplication, "multiplication"),
            4: (self.division, "division"),
        }

        op = operations.get(self.number_selection)

        if not op:
            print("Option not supported.")
            return

        func, name = op
        a, b = self.ask_two_numbers(name)

        try:
            result = func(a, b)
        except ZeroDivisionError:
            print("Error: división por cero.")
            return

        print(f"The result of the {name} is: {result}")


    def ask_int(self, prompt: str) -> int:
        while True:
            try:
                return Utilities.convert_to_int(input(prompt).strip())
            except ValueError:
                print("Entrada inválida. Introduce un número entero válido.")


    def ask_two_numbers(self, operation_name: str) -> Tuple[int, int]:
        a = self.ask_int(f"Please enter the first number of the {operation_name}: ")
        b = self.ask_int(f"Please enter the second number of the {operation_name}: ")

        return a, b

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
