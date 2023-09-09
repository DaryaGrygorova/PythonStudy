"""An example of using a function imported from the module"""

from module_1 import greeting

user_name = input('Please enter your name: \n').capitalize()

print(greeting(user_name))
