from typing import Optional, Any

num: int = 10
num_2: int = 5
num_3: int = 2

# Sum Operation
print("The value of the sum is: ", num + num_2)

# Rest Operation
print("The value of the rest is: ", num - num_2)

# Multiplication Operation
print("The value of the multiplication is: ", num * num_2)

# Division Operation
print("The value of the division is: ", num / num_2)

# Modulus Operation
print("The value of the modulus is: ", num % num_2)

# Exponentiation Operation
print("The value of the exponentiation is: ", num ** num_2)

# Floor Division Operation
print("The value of the floor division is: ", num // num_2)

# Augmented Assignment Operations
num += num_2
print("The value after augmented addition is: ", num)

num -= num_3
print("The value after augmented subtraction is: ", num)

num *= num_3
print("The value after augmented multiplication is: ", num)

# Comparison Operators
print("Is num equal to num_2? ", num == num_2)
print("Is num not equal to num_2? ", num != num_2)
print("Is num greater than num_2? ", num > num_2)
print("Is num less than num_2? ", num < num_2)
print("Is num greater than or equal to num_2? ", num >= num_2)
print("Is num less than or equal to num_2? ", num <= num_2)
