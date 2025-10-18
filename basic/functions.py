from typing import Optional, Any
from functools import partial, wraps
import time
import asyncio

# Functions

num: int = 10
num2: int = 20

def sum(a: int, b: int) -> int:
    return a + b

print("The sum is: ", sum(num, num2))

def greet(name: str = "mundo") -> str:
    """Ejemplo de parámetro con valor por defecto y docstring."""
    return f"hola, {name}"

def append_item(item, lst=None):
    """Evita el pitfall de mutables como valor por defecto."""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

def sum_all(*nums):
    """`*args`: suma n argumentos posicionales."""
    return sum(nums)

def build_person(name, **info):
    """`**kwargs`: construye un dict con datos extra."""
    person = {"name": name}
    person.update(info)
    return person

def divide(a, b, /, *, round_digits=2):
    """Ejemplo de parámetros solo-posicional (`/`) y solo-por-palabra (`*`)."""
    return round(a / b, round_digits)

def make_multiplier(n):
    """Closure: devuelve una función que multiplica por n."""
    def multiplier(x):
        return x * n
    return multiplier

def debug(func):
    """Decorador simple que imprime entrada/salida."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"DEBUG: llamando {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"DEBUG: {func.__name__} -> {result}")
        return result
    return wrapper

@debug
def apply_twice(func, x):
    """High-order function: recibe otra función y la aplica dos veces."""
    return func(func(x))

def countdown(n):
    """Generador: produce valores con `yield`."""
    while n > 0:
        yield n
        n -= 1

async def async_wait_and_return(val, delay=0.1):
    """Función asíncrona de ejemplo (usar con `await`)."""
    await asyncio.sleep(delay)
    return val

# Ejemplos de uso
if __name__ == "__main__":
    print(add(2, 3))
    print(greet())
    print(append_item(1))
    print(append_item(2, []))
    print(sum_all(1, 2, 3, 4))
    print(build_person("Ana", age=30, city="Madrid"))
    print(divide(10, 3, round_digits=3))
    doubler = make_multiplier(2)
    print(doubler(5))
    print(apply_twice(lambda x: x + 1, 3))

    for i in countdown(3):
        print("count:", i)

    # partial para fijar argumentos
    add5 = partial(add, 5)
    print(add5(10))

    # async demo (rápido)
    res = asyncio.run(async_wait_and_return("listo", 0.01))
    print(res)