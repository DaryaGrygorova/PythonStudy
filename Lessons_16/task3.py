"""Task 2- Product Store
Write a class Product that has three attributes: type, name, price.
Then create a class ProductStore, which will have some Products and
will operate with all products in the store. All methods,
in case they can’t perform its action, should raise ValueError
with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:
- add(product, amount) - adds a specified quantity of a single product
with a predefined price premium for your store(30 percent)
- set_discount(identifier, percent, identifier_type='name') - adds a discount
for all products specified by input identifiers (type or name). The discount must be specified
in percentage
- sell_product(product_name, amount) - removes a particular amount of products from the store
if available, in other case raises an error.
It also increments income if the sell_product method succeeds.
- get_income() - returns amount of many earned by ProductStore instance.
- get_all_products() - returns information about all available products in the store.
- get_product_info(product_name) - returns a tuple with product name
and amount of items in the store.
"""


class Product:
    """Product object with attributes: type, name, price"""

    def __init__(self, prod_type, prod_name, price):
        self.type = prod_type
        self.name = prod_name
        self.price = price

    def __repr__(self):
        return f"'name': {self.name}, 'type': {self.type}, 'price': {self.price}"


class ProductStore:
    """Prototype of store, with methods for operate with all products in the store"""

    def __init__(self, discount=30):
        self.storage = {}
        self.categories_set = {}
        self.discount = discount
        self.income = 0

    def create_storage_item(self, product, amount):
        """Create object for new entry in storage, add name of product in categories_set"""
        if product.type not in self.categories_set:
            self.categories_set[product.type] = set(product.name)
        else:
            self.categories_set[product.type].add(product.name)

        return {
            "product": product,
            "amount": amount,
            "discount": self.discount,
        }

    def add(self, product, amount):
        """Adds a specified quantity of a single product
        with a predefined price premium for your store(30 percent)."""
        if not isinstance(product, Product):
            raise ValueError("Invalid product type")
        if not isinstance(amount, int) or isinstance(amount, float) or amount <= 0:
            raise ValueError("Invalid amount value")
        if product.name not in self.storage:
            self.storage[product.name] = self.create_storage_item(product, amount)
        else:
            self.storage[product.name]["amount"] = (
                self.storage[product.name][product].get("amount", 0) + amount
            )

    def set_discount(self, identifier, percent, identifier_type="name"):
        """Adds a discount for all products specified by input identifiers
        (type or name). The discount must be specified in percentage."""
        if not isinstance(identifier, str) or len(identifier) == 0:
            raise ValueError("Invalid identifier value")
        if not isinstance(percent, int):
            raise ValueError("Invalid percent value")
        success = 0
        if identifier_type == "name":
            self.storage[identifier]["discount"] = percent
            success = 1
        else:
            for product_name in self.categories_set[identifier]:
                self.storage[product_name]["discount"] = percent
                success = 1
        if success == 0:
            raise ValueError(
                f"Product with {identifier_type}: '{identifier}' not found"
            )

    def sell_product(self, product_name, amount):
        """Removes a particular amount of products from the store if
        available, in other case raises an error. It also increments
        income if the sell_product method succeeds."""
        if product_name not in self.storage:
            raise ValueError(f"Product with name: '{product_name}' not found")
        if (
            not isinstance(amount, int)
            or isinstance(amount, float)
            or amount <= 0
            or self.storage[product_name]["amount"] - amount < 0
        ):
            raise ValueError("Invalid amount value")
        self.storage[product_name]["amount"] -= amount
        self.income = (
            self.storage[product_name]["product"].price
            * (1 - self.storage[product_name]["discount"] / 100)
            * amount
        )

    def get_income(self):
        """Returns amount of many earned by ProductStore instance."""
        return self.income

    def get_all_products(self):
        """Returns information about all available products in the store."""
        return self.storage

    def get_product_info(self, product_name):
        """Returns a tuple with product name and amount of items in the store."""
        if product_name not in self.storage:
            raise ValueError(f"Product with name: '{product_name}' not found")
        return product_name, self.storage[product_name].get("amount", 0)


p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
print("Products in storage with default discount:", s.get_all_products(), sep="\n")
s.set_discount("Ramen", 40)
s.sell_product("Ramen", 10)
print(
    'Products in storage with 40% discount for "Ramen":', s.get_all_products(), sep="\n"
)
print('Store income after selling 10 items of "Ramen":', s.get_income())

assert s.get_product_info("Ramen") == ("Ramen", 290)
assert s.get_income() == 9.0
