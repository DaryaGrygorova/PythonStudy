# Task 2
# Compute the total price of the stock where the total price
# is the sum of the price of an item multiplied by the quantity
# of this exact item.

# Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for product in stock:
    if (
        isinstance(stock[product], float | int)
        and isinstance(prices[product], float | int)
    ):
        total_price += stock[product] * prices[product]
    else:
        print(
            f'Error! Wrong data for {product}. '
            'Quantity and price must be numeric values\n',
            f'count in stock: {stock[product]}, {type(stock[product])}\n',
            f'price: {prices[product]}, {type(prices[product])}',
            sep=''
        )
        exit()

print('The total price of goods:', total_price)
