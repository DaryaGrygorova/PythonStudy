"""Task 2 - The sys module.
The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python? If so, does it affect where
Python looks for module files? Run some interactive tests to find it out."""

import sys

print(sys.path)
# Type of variable path is list, that why we can change it from within Python
print(f'Type of "sys.path": {type(sys.path)}', "\n")

# We can add an entry for a new directory to the 'sys.path' or remove it.
# But we must remember that sys.path plays a role in importing modules:

print(
    "Try import modules from directory task2, that includes files: math.py, random.py, module.py:\n"
)

PATH_DIRECTORY = sys.path.pop(0)
print(
    f"Try import module.py after deleting first element from sys.path ({PATH_DIRECTORY}):"
)
try:
    import module
except ModuleNotFoundError:
    print("Module not found!")
else:
    print("Module was imported successful")

print("Try import math.py after deleting first element from sys.path:")
try:
    import math
except ModuleNotFoundError:
    print("Module not found!")
else:
    print("Build-in module math was imported")

sys.path.insert(0, PATH_DIRECTORY)
print(
    "\nTry import module.py after adding element, that has been removed from sys.path:"
)
try:
    import module
except ModuleNotFoundError:
    print("Module not found!")
else:
    print("Module was imported successful")

print(
    "\nTry import build-in module random after adding element, that has been removed from sys.path"
)
try:
    import random
except ModuleNotFoundError:
    print("Module not found!")
else:
    print("Module was imported successful")
