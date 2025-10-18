# Class statements

class Person:
    persons: int = 0


    def __init__(self, name: str, lastname: str,age: int) -> None:
        self.name: str = name
        self.lastname: str = lastname
        self.age: int = age
        Person.persons += 1

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.lastname}"


instance = Person("John", "Doe", 30)
print("The first person data is: ", instance.name, instance.age)
print("Full name: ", instance.full_name)
print("Total persons: ", Person.persons)