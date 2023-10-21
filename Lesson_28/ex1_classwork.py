"""
Hash algorithm properties:
1. "Avalanche effect" - the tiniest change in incoming data changes the result completely
2. The possibility of each resulting checksum (hash) is the same to any other
3. You can not recreate the original contents from the checksum easily
"""


def my_hash(key_str: str):
    """Returns Hash for key string"""
    hash_value = 17

    for char in key_str:
        hash_value = (hash_value * 31 + ord(char)) % 100

    return hash_value


class HashTable:
    """Implementation of HastTable"""
    def __init__(self):
        self.storage = [[]] * 100 # result = [[], [], []]
        self.len = 0

    def get_by_key(self, my_key):
        """Returns value by key"""
        index = my_hash(my_key)
        result = self.storage[index]         # result = [[]]
        for item_key, item_value in result:  # result = [[key, value]] -> result[0][1] = value
            if item_key == my_key:
                return item_value
        raise KeyError

    def save_value_by_key(self, my_key, new_value):
        """Add item with key "key" to HashTable"""
        self.len += 1
        self.storage_extend()
        index = my_hash(my_key)
        # collision processing
        result = self.storage[index]   # result = [[key, value], [key1, value1]] -> result[0][0][1] = value
        for inner_index, (item_key, item_value) in enumerate(result):
            if item_key == my_key:
                self.storage[index][inner_index][1] = item_value
                return None
        self.storage[index].append([my_key, new_value])
        return None

    def delete_item_by_key(self, my_key):
        """Delete item from storage by key"""
        index = my_hash(my_key)
        result = self.storage[index]  # result = [[key, value], [key1, value1]] -> result[0][0][1] = value

        for inner_index, (item_key, _) in enumerate(result):
            if item_key == my_key:
                self.storage[index].pop(inner_index)
                self.len -= 1
                return
        raise KeyError

    def __contains__(self, item):
        """Returns True if table contains key that equal item"""
        # value in HashTable() -> __contains__(HashTable(), value)
        index = my_hash(item)
        result = self.storage[index]  # result = [[key, value], [key1, value1]] -> result[0][0][1] = value

        for item_key, _ in result:
            if item_key == item:
                return True
        return False

    def items(self):
        """Returns list with items"""
        return [[*nested_lists] for nested_lists in self.storage]

    def table_update(self, other_table):
        """Append new items to Table"""
        for item_key, item_value in other_table.items():
            self.save_value_by_key(item_key, item_value)

    def __len__(self):
        return self.len

    def __getitem__(self, item_key):
        index = my_hash(item_key)
        result = self.storage[index]  # result = [[key, value], [key1, value1]] -> result[0][0][1] = value

        for key, value in result:
            if item_key == key:
                return value
        raise KeyError

    def __setitem__(self, item_key, new_value):
        self.save_value_by_key(item_key, new_value)

    def storage_extend(self):
        if self.len == len(self.storage):
            new_storage = [[]] * self.len*2
            pass


# 1. collissions processing
# 2. deletion operator
# 3. get length  __len__
# 4. "in" operator  __contains__
# 5. "update" operator
# 6. turn methods into magic methods


my_dict = HashTable()
my_dict["key"] = 'new value'

print(my_dict["key"])
