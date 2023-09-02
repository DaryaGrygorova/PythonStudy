"""Build in function"""


def factory_sum():
    """Return another function that advice two numbers"""

    def sum_numbers(num_1, num_2):
        """Advice two numbers"""
        return num_1 + num_2

    return sum_numbers


print(factory_sum()(3, 2))
