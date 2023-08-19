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

