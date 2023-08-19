# Task 3
# Write a program, which has two print statements to print the following text 
# (capital letters "O" and "H", made from "#" symbols):
# #########
# #       #
# #       #
# #       #
# #########

# #       #
# #       #
# #########
# #       #
# #       #

# Pay attention that usage of spaces is forbidden, as well as creating the whole result 
# text string using """ """, use '\n' and '\t' symbols instead.

symbol = '#'
str_with_two_symbols = f'{symbol}\t{symbol}'

# print "O", made from "#" symbols
print(
    symbol*9, 
    str_with_two_symbols, 
    str_with_two_symbols, 
    str_with_two_symbols, 
    symbol*9, 
    sep="\n",
    end="\n\n"
    )


# print "H", made from "#" symbols
print(
    str_with_two_symbols, 
    str_with_two_symbols, 
    symbol*9, 
    str_with_two_symbols, 
    str_with_two_symbols, 
    sep="\n"
    )

