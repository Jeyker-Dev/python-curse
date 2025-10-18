# python
from copy import deepcopy

# Creación
d = {"a": 1, "b": 2}           # literal
d2 = dict(c=3, d=4)           # constructor
comp = {k: k.upper() for k in ["x", "y"]}  # comprehension

# Acceso seguro y asignación
val = d.get("z", 0)           # devuelve 0 si no existe
d["e"] = 5                    # inserta/actualiza

# setdefault: obtiene o crea con valor por defecto
d.setdefault("f", 6)          # si "f" no existe lo crea con 6

# Eliminación
x = d.pop("a", None)          # elimina y devuelve, o None si no existe
k, v = d.popitem()            # elimina el último par (LIFO en 3.7+)

# Iteración
for key in d:
    pass                      # itera claves (orden de inserción)
for key, value in d.items():
    pass                      # itera pares

# Vistas dinámicas
ks = d.keys()                 # vista de claves (refleja cambios)
vs = d.values()

# Fusión (no destructiva) y update (destructiva)
merged = d | d2               # Python 3.9+: claves de d2 sobrescriben d
d.update(d2)                  # actualiza d in-place

# Copias: superficial vs profunda
shallow = d.copy()
deep = deepcopy(d)            # útil si hay estructuras mutables anidadas

# Uso de tuplas como claves
coords = {(0, 0): "origen", (1, 2): "punto"}

# Convertir listas de pares a dict
pairs = [("k1", 10), ("k2", 20)]
from_pairs = dict(pairs)

# Ejemplo práctico: contar ocurrencias
words = ["a", "b", "a", "c"]
counter = {}
for w in words:
    counter[w] = counter.get(w, 0) + 1

# Nota: evitar sobrescribir builtins
my_dict = {}  # no usar nombre `dict` ni `list` ni `set`
