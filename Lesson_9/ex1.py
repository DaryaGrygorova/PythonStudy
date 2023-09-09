"""" """

NUM = 1
NUM_2 = 1

print(NUM == NUM_2) # True - checks value
print(NUM is NUM_2) # True - checks value, type, id in memory

# для економії пам'яті малі за об'ємом пам'яті незмінні змінні записуються
# в одну комірку пам'яті та у змінну передається лише посилання на неї
print(id(NUM) == id(NUM_2))   # True - checks value

print(id(NUM) is id(NUM_2))
# False - самі числа, що повернулися з id() знаходиться у різних комірках

print(id(NUM))
print(id(NUM_2))
