import array
from typing import Optional,Any

count: int = 5
total: int = 0
numbers: list[int] = [10, 20, 30, 40, 50]

# For Loop
for i in range(1, count + 1):
    total += i
print("The total sum from 1 to", count, "is:", total)

for char in "Hello":
    print("Character:", char)

for i in numbers:
    print("Number from array:", i)

# While Loop

while total > 0:
    print("Current total is:", total)
    total -= 10
